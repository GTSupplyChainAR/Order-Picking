'use strict';

/**
 * @ngdoc function
 * @name visualizationApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the visualizationApp
 */

angular.module('visualizationApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.start = null;
    $scope.end = null;
    $scope.activeTool = 'shelf';
    $scope.x = 5;
    $scope.y = 10;

    $scope.resetGrid = function(x, y){
      $scope.grid = [];
      for (var i = 0; i < $scope.x; i++) {
        $scope.grid[i] = [];
        for (var j = 0; j < $scope.y; j++) {
          $scope.grid[i][j] = {
            'type': 'floor',
            'x': i,
            'y': j
          };
        }
      }
    }

    function setStart(x, y){
      if($scope.start !== null){
        var old_x = $scope.start.x
        var old_y = $scope.start.y
        $scope.grid[old_x][old_y].type = 'floor';
      }
      $scope.start = {x: x, y: y};
      $scope.grid[x][y].type = 'start';
    }

    function setEnd(x, y){
      if($scope.end !== null){
        var old_x = $scope.end.x
        var old_y = $scope.end.y
        $scope.grid[old_x][old_y].type = 'floor';
      }
      $scope.end = {x: x, y: y};
      $scope.grid[x][y].type = 'end';

    }

    function setFloor(x, y){
      if($scope.grid[x][y].type === 'start'){
        $scope.start = null;
      }
      if($scope.grid[x][y].type === 'end'){
        $scope.end = null;
      }

      $scope.grid[x][y].type = 'floor';
    }

    function setShelf(x, y){
      if($scope.grid[x][y].type === 'start'){
        $scope.start = null;
      }
      if($scope.grid[x][y].type === 'end'){
        $scope.end = null;
      }

      $scope.grid[x][y].type = 'shelf';
    }

    $scope.squareClick = function(cell){
      if($scope.activeTool === 'shelf'){
        setShelf(cell.x, cell.y);
      }

      if($scope.activeTool === 'floor'){
        setFloor(cell.x, cell.y);
      }

      if($scope.activeTool === 'start'){
        setStart(cell.x, cell.y);
      }

      if($scope.activeTool === 'end'){
        setEnd(cell.x, cell.y);
      }
    }

    $scope.findPath = function(){
      var walls = []
      for (var i = 0; i < $scope.x; i++) {
        for (var j = 0; j < $scope.y; j++) {
          if($scope.grid[i][j].type === 'shelf'){
            walls.push([i, j]);
          }
        }
      }

      var payload = {
        "start": [$scope.start.x, $scope.start.y], 
        "end": [$scope.end.x, $scope.end.y],
        "rows": $scope.x,
        "cols": $scope.y,
        "walls": walls
      }
      var url = 'http://127.0.0.1:5000?info=' + JSON.stringify(payload)

      $http.get(url).then(function(response){
        for (var i = 1; i < response.data.length - 1; i++) {
          var x = response.data[i][0];
          var y = response.data[i][1];
          $scope.grid[x][y].type = 'path';
        }
      });
    }

    $scope.resetGrid();

  });
