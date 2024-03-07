using System;
//ATIVIDADE 1

using System;

public class Test
{
    public static void Main()
    {
        int INDICE = 13;
        int SOMA = 0;
        int K = 0;

        while (K < INDICE)
        {
            K = K + 1;
            SOMA = SOMA + K;
        }
        Console.WriteLine(SOMA);
    }
}


//ATIVIDADE 2

public class Program
{
    public void Run()
    {
        bool Raiz(int n)
        {
            int s = (int)Math.Sqrt(n);
            return s * s == n;
        }

        bool Fibonacci(int n)
        {
            return Raiz(5 * n * n + 4) || Raiz(5 * n * n - 4);
        }

        public class Program
        {
            public static void Main()
            {
                Console.Write("Digite um número: ");
                int num = int.Parse(Console.ReadLine());

                if (Fibonacci(num) == true)
                {
                    Console.WriteLine($"{num} pertence à sequência de Fibonacci.");
                }
                else
                {
                    Console.WriteLine($"{num} não pertence à sequência de Fibonacci.");
                }
            }
        }
    }
}
//obs: coloquei um imput para inserir o numero e verificar se é ou não da sequencia.


//ATIVIDADE 3
using System;

public class Test
{
    public static void Main()
    {
        string s = "Olá, mundo!";

        char[] array = s.ToCharArray();
        Array.Reverse(array);
        string inverso = new string(array);

        Console.WriteLine(inverso);
    }
}
