
class MyList
{
    public class Node
    {
        public Node? left;
        public Node? right;
        public int value;

        public Node(Node? left, Node? right, int value)
        {
            this.left = left;
            this.right = right;
            this.value = value;
        }

        public Node(int value)
        {
            this.value = value;
        }

        public override string ToString()
        {
            return value.ToString();
        }

    }

    Node? tail = null;
    Node? head = null;
    public Dictionary<int,Node> values = new Dictionary<int,Node>();
    int size = 0;

    public void add(int value)
    {
        if(tail == null && head == null)
        {
            Node node = new Node(value);
            tail = node;
            head = node;
            values.Add(size, node);
            size++;
        }
        else
        {
            Node NewNode = new Node(null,head,value);
            head.left = NewNode;
            head = NewNode;
            values.Add(size, NewNode);
            size++;
        }
    }


    public void remove(int value)
    {
        if(tail==null && head == null)
        {
            throw new Exception("Linked list is empty");
        }
        else
        {
            foreach(int id in values.Keys)
            {
                if (values[id].value == value)
                {
                    values.Remove(id);
                    size--;
                }
            }
        }

        int index = 0;
        Dictionary<int,Node> NewDict = new Dictionary<int,Node>();
        foreach (var item in values.Values)
        {
            NewDict[index] = item;
            index++;
        }
        values = NewDict;
    }

    public override string ToString()
    {
        string res = "";
        foreach(var elem in values)
        {
            res += elem.ToString();
        }
        return res;
    }

}



class Programm
{
    static void Main(string[] args)
    {

        MyList x = new MyList();
        x.add(1);
        x.add(2);
        x.add(3);
        x.add(1);
        Console.WriteLine("added elements :");
        foreach(var elem in x.values)
        {
            Console.WriteLine(elem);
        }
        x.remove(1);
        x.remove(3);
        Console.WriteLine("elements after deletion :");
        foreach(var elem in x.values)
        {
            Console.WriteLine(elem);
        }
        x.add(1);
        x.add(2);
        x.add(3);
        x.add(1);
        Console.WriteLine("added elements :");
        foreach (var elem in x.values)
        {
            Console.WriteLine(elem);
        }
    }

}