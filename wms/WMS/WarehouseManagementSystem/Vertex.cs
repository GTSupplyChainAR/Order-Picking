using System;
/*
 * Class representing a Vertex. To be used inside a Graph.
 */

namespace WarehouseManagementSystem
{
    public class Vertex
    {
        private T data;
        public Vertex(T data)
        {
            if (data == null)
            {
                throw new ArgumentException("Data is null");
            }
            this.data = data;
        }
    }

    public bool equals(Object o)
    {
        if (o != null && o instanceof Vertex)
        {
            return data.equals(((Vertex <?>) o).data);
        } else {
            return false;
        }
    }

    @Override
    public int hashCode()
    {
        return data.hashCode();
    }

    /**
     * Gets the data in this vertex.
     *
     * @return the data in this vertex
     */
    public T getData()
    {
        return data;
    }

    @Override
    public String toString()
    {
        return data.toString();
    }

}
