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
        $scope.resetGrid = function(x, y){
            $scope.start = null;
            $scope.paths = null;
            $scope.step = 0;

            $scope.activeTool = 'shelf';
            $scope.x = 5;
            $scope.y = 10;
            $scope.grid = [];
            for (var i = 0; i < $scope.x; i++) {
                $scope.grid[i] = [];
                for (var j = 0; j < $scope.y; j++) {
                    $scope.grid[i][j] = {
                        'type': 'floor',
                        'x': i,
                        'y': j,
                        'path': false
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
            if($scope.grid[x][y].type === 'start'){
                $scope.start = null;
            }

            $scope.grid[x][y].type = 'end';
        }

        function setFloor(x, y){
            if($scope.grid[x][y].type === 'start'){
                $scope.start = null;
            }

            $scope.grid[x][y].type = 'floor';
        }

        function setShelf(x, y){
            if($scope.grid[x][y].type === 'start'){
                $scope.start = null;
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

        $scope.setPath = function(){
            for (var i = 0; i < $scope.x; i++) {
                for (var j = 0; j < $scope.y; j++) {
                    $scope.grid[i][j].path = false;
                }
            }

            for (var i = 1; i < $scope.paths[$scope.step].length; i++) {
                var box = $scope.paths[$scope.step][i]
                $scope.grid[box[0]][box[1]].path = true;
            }
        }

        $scope.setStep = function(step){
            $scope.step = step;
            $scope.setPath();
        }

        $scope.findPath = function(){
            var walls = []
            var ends = []
            for (var i = 0; i < $scope.x; i++) {
                for (var j = 0; j < $scope.y; j++) {
                    if($scope.grid[i][j].type === 'end'){
                        ends.push([i, j]);
                    }
                    if($scope.grid[i][j].type === 'shelf'){
                        walls.push([i, j]);
                    }
                }
            }

            var payload = {
                "start": [$scope.start.x, $scope.start.y], 
                "end": ends,
                "rows": $scope.x,
                "cols": $scope.y,
                "walls": walls
            }
            var url = 'http://127.0.0.1:5000?info=' + JSON.stringify(payload)

            $http.get(url).then(function(response){
                $scope.paths = response.data;
                $scope.setStep(0);
            });
        }

        $scope.resetGrid();
    });
