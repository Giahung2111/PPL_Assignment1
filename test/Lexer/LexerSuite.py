
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_01(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "VO\nTIEN\n" ""","Unclosed string: \"VO", '01'))

    def test_02(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", '02' ))
    def test_100(self):
        self.assertTrue(TestLexer.test(
            """var i int = s[2][2].callFunc(f1(2 + 2, abc)) + "strc";""",
            "var,i,int,=,s,[,2,],[,2,],.,callFunc,(,f1,(,2,+,2,,,abc,),),+,strc,;,<EOF>",
            100
        ))

    def test_101(self):
        self.assertTrue(TestLexer.test(
            """x + y ;
            3.14
            a * b - c ;""",
            "x,+,y,;,3.14,;,a,*,b,-,c,;,<EOF>",
            101
        ))

    def test_102(self):
        self.assertTrue(TestLexer.test(
            "\"hello world\" \n putInt( x + y ) ; \n getString ( ) ;",
            "hello world,;,putInt,(,x,+,y,),;,getString,(,),;,<EOF>",
            102
        ))

    def test_103(self):
        self.assertTrue(TestLexer.test(
            "if ( x > 0 ) { return x ; } \n for ( int i = 0 ; i < 10 ; i += 1) { return i ; }",
            "if,(,x,>,0,),{,return,x,;,},;,for,(,int,i,=,0,;,i,<,10,;,i,+=,1,),{,return,i,;,},<EOF>",
            103
        ))

    def test_104(self):
        self.assertTrue(TestLexer.test(
            "func foo ( x int , y int ) { return x + y ; } \n",
            "func,foo,(,x,int,,,y,int,),{,return,x,+,y,;,},;,<EOF>",
            104
        ))
        
    def test_105(self):
        self.assertTrue(TestLexer.test(
            """
            var x int ;
            const y float = 3.14 ;
            func add(a int, b int) int {
                return a + b ;
            }
            x = y + 10
            """,
            "var,x,int,;,const,y,float,=,3.14,;,func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},;,x,=,y,+,10,;,<EOF>",
            105
        ))

    def test_106(self):
        self.assertTrue(TestLexer.test(
            """
            func foo( x int , y int ) { return x + y ; }
            var a = 10 ;
            3.14
            """,
            "func,foo,(,x,int,,,y,int,),{,return,x,+,y,;,},;,var,a,=,10,;,3.14,;,<EOF>",
            106
        ))

    def test_107(self):
        self.assertTrue(TestLexer.test(
            """
            if (x > 0) {
                for (i = 0 ; i < 10 ; i += 1) {
                    putInt( i );
                }
            } else {
                return false
            }""",
            "if,(,x,>,0,),{,for,(,i,=,0,;,i,<,10,;,i,+=,1,),{,putInt,(,i,),;,},;,},else,{,return,false,;,},<EOF>",
            107
        ))

    def test_108(self):
        self.assertTrue(TestLexer.test(
            """
            var int = 123 ;
            func test(x int, y float) {
                return x / y ;
            }
            const z boolean = true && false ;
            """,
            "var,int,=,123,;,func,test,(,x,int,,,y,float,),{,return,x,/,y,;,},;,const,z,boolean,=,true,&&,false,;,<EOF>",
            108
        ))

    def test_109(self):
        self.assertTrue(TestLexer.test(
            """
            putStringLn( "Hello, world!" );
            putIntLn(x + y) ;
            func invalidFunc( ) { return ; }
            for (int i = 0 ; i < 10 ; i += 1 ) {
                // missing initialization
            }""",
            """putStringLn,(,Hello, world!,),;,putIntLn,(,x,+,y,),;,func,invalidFunc,(,),{,return,;,},;,for,(,int,i,=,0,;,i,<,10,;,i,+=,1,),{,},<EOF>""",
            109
        ))
    
    def test_110(self):
        self.assertTrue(TestLexer.test(
            """
            type Point struct {
                x int ;
                y int ;
            }

            func (p Point) distance( ) float {
                return sqrt(p.x * p.x + p.y * p.y) ;
            }

            func main( ) {
                var p Point = Point{3, 4} ;
                putFloatLn( p.distance( ) );
            }""",
            "type,Point,struct,{,x,int,;,y,int,;,},;,func,(,p,Point,),distance,(,),float,{,return,sqrt,(,p,.,x,*,p,.,x,+,p,.,y,*,p,.,y,),;,},;,func,main,(,),{,var,p,Point,=,Point,{,3,,,4,},;,putFloatLn,(,p,.,distance,(,),),;,},<EOF>",
            110
        ))

    def test_111(self):
        self.assertTrue(TestLexer.test(
            """
            var x int = 10 \n
            var y float = 3.14 \n
            var z string = "hello";
            """,
            "var,x,int,=,10,;,var,y,float,=,3.14,;,var,z,string,=,hello,;,<EOF>",
            111
        ))
        
    def test_112(self):
        self.assertTrue(TestLexer.test(
            """
            0x12 ;
            0x123GH ;
            """,
            "0x12,;,0x123,GH,;,<EOF>",
            112
        ))
        
    def test_113(self):
        self.assertTrue(TestLexer.test(
            "abc /* unclosed comment", 
            "abc,/,*,unclosed,comment,<EOF>", 
            113
        ))
        
    def test_114(self):
        self.assertTrue(TestLexer.test(
            "@_ @a @13",
            "ErrorToken @",
            114
        ))
        
    def test_115(self):
        self.assertTrue(TestLexer.test(
            "/* test1 \n //test2 \n /*test3*/ asdasdas */",
            "<EOF>",
            115
        ))
        
    def test_116(self):
        self.assertTrue(TestLexer.test(
            "1234 0 9876",
            "1234,0,9876,<EOF>",
            116
        ))
    
    def test_117(self):
        self.assertTrue(TestLexer.test(
            """ "valid string" "invalid string 
            """,
            "valid string,Unclosed string: \"invalid string ", 
            117
        ))
    
    def test_118(self):
        self.assertTrue(TestLexer.test(
            "func main() { return 0x1A3F; }",
            "func,main,(,),{,return,0x1A3F,;,},<EOF>",
            118
        ))
    
    def test_119(self):
        self.assertTrue(TestLexer.test(
            "/* This is a block comment */ var x = 10;",
            "var,x,=,10,;,<EOF>",
            119
        ))
    
    def test_120(self):
        self.assertTrue(TestLexer.test(
            "! && || == != < > <= >=",
            "!,&&,||,==,!=,<,>,<=,>=,<EOF>",
            120
        ))
    
    def test_121(self):
        self.assertTrue(TestLexer.test(
            """ var arr = [1, 2, 3, 4]; """,
            "var,arr,=,[,1,,,2,,,3,,,4,],;,<EOF>",
            121
        ))
    
    def test_122(self):
        self.assertTrue(TestLexer.test(
            "const PI = 3.14159;",
            "const,PI,=,3.14159,;,<EOF>",
            125
        ))
    
    def test_123(self):
        self.assertTrue(TestLexer.test(
            """putStringLn("Escape \\" test\\"")""",
            """putStringLn,(,Escape \\" test\\",),<EOF>""",
            123
        ))
    
    def test_124(self):
        self.assertTrue(TestLexer.test(
            "while (x != 0) { x -= 1; }",
            "while,(,x,!=,0,),{,x,-=,1,;,},<EOF>",
            124
        ))
        
    def test_125(self):
        self.assertTrue(TestLexer.test(
            """
            var a int = 10;
            var b float = 20.5;
            var c string = "Hello, MiniGo!";
            var d boolean = true;
            """,
            "var,a,int,=,10,;,var,b,float,=,20.5,;,var,c,string,=,Hello, MiniGo!,;,var,d,boolean,=,true,;,<EOF>",
            125
        ))

    def test_126(self):
        self.assertTrue(TestLexer.test(
            """
            func factorial(n int) int {
                if n == 0 {
                    return 1;
                }
                return n * factorial(n - 1);
            }""",
            "func,factorial,(,n,int,),int,{,if,n,==,0,{,return,1,;,},;,return,n,*,factorial,(,n,-,1,),;,},<EOF>",
            126
        ))

    def test_127(self):
        self.assertTrue(TestLexer.test(
            """
            type Person struct {
                name string;
                age int;
            }

            func main() {
                var p Person = Person{"Alice", 25};
                putStringLn(p.name);
                putIntLn(p.age);
            }""",
            "type,Person,struct,{,name,string,;,age,int,;,},;,func,main,(,),{,var,p,Person,=,Person,{,Alice,,,25,},;,putStringLn,(,p,.,name,),;,putIntLn,(,p,.,age,),;,},<EOF>",
            127
        ))

    def test_128(self):
        self.assertTrue(TestLexer.test(
            """
            func fibonacci(n int) int {
                var a int = 0;
                var b int = 1;
                for i := 0; i < n; i += 1 {
                    var temp int = a + b;
                    a = b;
                    b = temp;
                }
                return a;
            }""",
            "func,fibonacci,(,n,int,),int,{,var,a,int,=,0,;,var,b,int,=,1,;,for,i,:=,0,;,i,<,n,;,i,+=,1,{,var,temp,int,=,a,+,b,;,a,=,b,;,b,=,temp,;,},;,return,a,;,},<EOF>",
            128
        ))

    def test_129(self):
        self.assertTrue(TestLexer.test(
            """
            var arr [5] int = [1, 2, 3, 4, 5];

            func sumArray(arr [5] int) int {
                var sum int = 0;
                for i := 0; i < 5; i += 1 {
                    sum += arr[i];
                }
                return sum;
            }""",
            "var,arr,[,5,],int,=,[,1,,,2,,,3,,,4,,,5,],;,func,sumArray,(,arr,[,5,],int,),int,{,var,sum,int,=,0,;,for,i,:=,0,;,i,<,5,;,i,+=,1,{,sum,+=,arr,[,i,],;,},;,return,sum,;,},<EOF>",
            129
        ))

    def test_130(self):
        self.assertTrue(TestLexer.test(
            """
            func main() {
                var x float = 5.25;
                var y float = 2.75;
                var result float = x * y + (x / y) - (x - y);
                putFloatLn(result);
            }""",
            "func,main,(,),{,var,x,float,=,5.25,;,var,y,float,=,2.75,;,var,result,float,=,x,*,y,+,(,x,/,y,),-,(,x,-,y,),;,putFloatLn,(,result,),;,},<EOF>",
            130
        ))

    def test_131(self):
        self.assertTrue(TestLexer.test(
            """
            var a, b, c int = 1, 2, 3;
            var d, e, f float = 1.1, 2.2, 3.3;
            var g, h, i string = "one", "two", "three";
            """,
            "var,a,,,b,,,c,int,=,1,,,2,,,3,;,var,d,,,e,,,f,float,=,1.1,,,2.2,,,3.3,;,var,g,,,h,,,i,string,=,one,,,two,,,three,;,<EOF>",
            131
        ))

    def test_132(self):
        self.assertTrue(TestLexer.test(
            """
            func power(base int, exp int) int {
                var result int = 1;
                for i := 0; i < exp; i += 1 {
                    result *= base;
                }
                return result;
            }""",
            "func,power,(,base,int,,,exp,int,),int,{,var,result,int,=,1,;,for,i,:=,0,;,i,<,exp,;,i,+=,1,{,result,*=,base,;,},;,return,result,;,},<EOF>",
            132
        ))

    def test_133(self):
        self.assertTrue(TestLexer.test(
            """
            func sumRange(start int, end int) int {
                var sum int = 0;
                for i := start; i <= end; i += 1 {
                    sum += i;
                }
                return sum;
            }""",
            "func,sumRange,(,start,int,,,end,int,),int,{,var,sum,int,=,0,;,for,i,:=,start,;,i,<=,end,;,i,+=,1,{,sum,+=,i,;,},;,return,sum,;,},<EOF>",
            133
        ))

    def test_134(self):
        self.assertTrue(TestLexer.test(
            """
            func gcd(a int, b int) int {
                while b != 0 {
                    var temp int = b;
                    b = a % b;
                    a = temp;
                }
                return a;
            }""",
            "func,gcd,(,a,int,,,b,int,),int,{,while,b,!=,0,{,var,temp,int,=,b,;,b,=,a,%,b,;,a,=,temp,;,},;,return,a,;,},<EOF>",
            134
        ))

    def test_135(self):
        input = """func main() {
            var sum int = 0;
            for i := 1; i <= 10; i += 1 {
                if (i % 2 == 0) {
                    sum += i;
                }
            }
            putIntLn(sum);
        }"""
        expect = "func,main,(,),{,var,sum,int,=,0,;,for,i,:=,1,;,i,<=,10,;,i,+=,1,{,if,(,i,%,2,==,0,),{,sum,+=,i,;,},;,},;,putIntLn,(,sum,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test_136(self):
        input = """type Student struct {
            name string;
            grades [3]int;
        }
        func main() {
            var s Student = Student{name: "Alice", grades: [3]int{90, 85, 88}};
            putStringLn(s.name);
            for i := 0; i < 3; i += 1 {
                putIntLn(s.grades[i]);
            }
        }"""
        expect = """type,Student,struct,{,name,string,;,grades,[,3,],int,;,},;,func,main,(,),{,var,s,Student,=,Student,{,name,:,Alice,,,grades,:,[,3,],int,{,90,,,85,,,88,},},;,putStringLn,(,s,.,name,),;,for,i,:=,0,;,i,<,3,;,i,+=,1,{,putIntLn,(,s,.,grades,[,i,],),;,},;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))
        
    def test_137(self):
        input = """func sort(arr [5]int) [5]int {
            var temp int;
            for i := 0; i < 5; i += 1 {
                for j := i + 1; j < 5; j += 1 {
                    if (arr[i] > arr[j]) {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
            return arr;
        }
        func main() {
            var nums [5]int = [5]int{5, 3, 4, 1, 2};
            var sorted [5]int = sort(nums);
            for i := 0; i < 5; i += 1 {
                putIntLn(sorted[i]);
            }
        }"""
        expect = "func,sort,(,arr,[,5,],int,),[,5,],int,{,var,temp,int,;,for,i,:=,0,;,i,<,5,;,i,+=,1,{,for,j,:=,i,+,1,;,j,<,5,;,j,+=,1,{,if,(,arr,[,i,],>,arr,[,j,],),{,temp,=,arr,[,i,],;,arr,[,i,],=,arr,[,j,],;,arr,[,j,],=,temp,;,},;,},;,},;,return,arr,;,},;,func,main,(,),{,var,nums,[,5,],int,=,[,5,],int,{,5,,,3,,,4,,,1,,,2,},;,var,sorted,[,5,],int,=,sort,(,nums,),;,for,i,:=,0,;,i,<,5,;,i,+=,1,{,putIntLn,(,sorted,[,i,],),;,},;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test_138(self):
        input = """type Student struct {
            name string;
            grades [5]int;
        }
        func (s Student) Average() float {
            var total int = 0;
            for i := 0; i < 5; i += 1 {
                total += s.grades[i];
            }
            return to_float(total) / 5.0;
        }
        func main() {
            var s Student = Student{name: "Bob", grades: [5]int{90, 85, 78, 92, 88}};
            var avg float = s.Average();
            putFloatLn(avg);
        }"""
        expect = "type,Student,struct,{,name,string,;,grades,[,5,],int,;,},;,func,(,s,Student,),Average,(,),float,{,var,total,int,=,0,;,for,i,:=,0,;,i,<,5,;,i,+=,1,{,total,+=,s,.,grades,[,i,],;,},;,return,to_float,(,total,),/,5.0,;,},;,func,main,(,),{,var,s,Student,=,Student,{,name,:,Bob,,,grades,:,[,5,],int,{,90,,,85,,,78,,,92,,,88,},},;,var,avg,float,=,s,.,Average,(,),;,putFloatLn,(,avg,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_139(self):
        input = """func findMax(arr [5]int) int {
            var max int = arr[0];
            for i := 1; i < 5; i += 1 {
                if (arr[i] > max) {
                    max = arr[i];
                }
            }
            return max;
        }
        func main() {
            var nums [5]int = [5]int{10, 20, 5, 30, 15};
            var maxValue int = findMax(nums);
            putIntLn(maxValue);
        }"""
        expect = "func,findMax,(,arr,[,5,],int,),int,{,var,max,int,=,arr,[,0,],;,for,i,:=,1,;,i,<,5,;,i,+=,1,{,if,(,arr,[,i,],>,max,),{,max,=,arr,[,i,],;,},;,},;,return,max,;,},;,func,main,(,),{,var,nums,[,5,],int,=,[,5,],int,{,10,,,20,,,5,,,30,,,15,},;,var,maxValue,int,=,findMax,(,nums,),;,putIntLn,(,maxValue,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_140(self):
        input = """type Point struct {
            x int;
            y int;
        }
        type Rectangle struct {
            topLeft Point;
            bottomRight Point;
        }
        func (r Rectangle) Area() int {
            var width int = r.bottomRight.x - r.topLeft.x;
            var height int = r.bottomRight.y - r.topLeft.y;
            return width * height;
        }
        func main() {
            var rect Rectangle = Rectangle{topLeft: Point{x: 1, y: 5}, bottomRight: Point{x: 4, y: 1}};
            var area int = rect.Area();
            putIntLn(area);
        }"""
        expect = "type,Point,struct,{,x,int,;,y,int,;,},;,type,Rectangle,struct,{,topLeft,Point,;,bottomRight,Point,;,},;,func,(,r,Rectangle,),Area,(,),int,{,var,width,int,=,r,.,bottomRight,.,x,-,r,.,topLeft,.,x,;,var,height,int,=,r,.,bottomRight,.,y,-,r,.,topLeft,.,y,;,return,width,*,height,;,},;,func,main,(,),{,var,rect,Rectangle,=,Rectangle,{,topLeft,:,Point,{,x,:,1,,,y,:,5,},,,bottomRight,:,Point,{,x,:,4,,,y,:,1,},},;,var,area,int,=,rect,.,Area,(,),;,putIntLn,(,area,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_141(self):
        input = """func main() {
            var a int = 3;
            var b int = 10;
            var c int = 7;
            if (a < b && b > c) {
                if (c > a) {
                    putStringLn("c is the largest among a, b, and c");
                }
            } else {
                putStringLn("b is not the largest");
            }
        }"""
        expect = """func,main,(,),{,var,a,int,=,3,;,var,b,int,=,10,;,var,c,int,=,7,;,if,(,a,<,b,&&,b,>,c,),{,if,(,c,>,a,),{,putStringLn,(,c is the largest among a, b, and c,),;,},;,},else,{,putStringLn,(,b is not the largest,),;,},;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_142(self):
        input = """type Employee struct {
            name string;
            salary float;
        }
        func increaseSalary(emp Employee, percent float) Employee {
            emp.salary += emp.salary * (percent / 100.0);
            return emp;
        }
        func main() {
            var emp Employee = Employee{name: "Alice", salary: 50000.0};
            emp = increaseSalary(emp, 10);
            putFloatLn(emp.salary);
        }"""
        expect = """type,Employee,struct,{,name,string,;,salary,float,;,},;,func,increaseSalary,(,emp,Employee,,,percent,float,),Employee,{,emp,.,salary,+=,emp,.,salary,*,(,percent,/,100.0,),;,return,emp,;,},;,func,main,(,),{,var,emp,Employee,=,Employee,{,name,:,Alice,,,salary,:,50000.0,},;,emp,=,increaseSalary,(,emp,,,10,),;,putFloatLn,(,emp,.,salary,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_143(self):
        input = """func main() {
            var chars [5]rune = [5]rune{\"H\", \"e\", \"l\", \"l\",\"o\"};
            var str string = "";
            for i := 0; i < 5; i += 1 {
                str += to_string(chars[i]);
            }
            putStringLn(str);
        }"""
        expect = "func,main,(,),{,var,chars,[,5,],rune,=,[,5,],rune,{,H,,,e,,,l,,,l,,,o,},;,var,str,string,=,,;,for,i,:=,0,;,i,<,5,;,i,+=,1,{,str,+=,to_string,(,chars,[,i,],),;,},;,putStringLn,(,str,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_144(self):
        input = """func main() {
            var count int = 10;
            for count > 0 {
                putIntLn(count);
                count = count - 1;
            }
            putStringLn("Countdown complete!");
        }"""
        expect = "func,main,(,),{,var,count,int,=,10,;,for,count,>,0,{,putIntLn,(,count,),;,count,=,count,-,1,;,},;,putStringLn,(,Countdown complete!,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_145(self):
        input = """type Car struct {
            model string;
            year int;
        }
        func (c Car) Info() string {
            return c.model + " (" + to_string(c.year) + ")";
        }
        func main() {
            var myCar Car = Car{model: "Toyota", year: 2021};
            var info string = myCar.Info();
            putStringLn(info);
        }"""
        expect = """type,Car,struct,{,model,string,;,year,int,;,},;,func,(,c,Car,),Info,(,),string,{,return,c,.,model,+, (,+,to_string,(,c,.,year,),+,),;,},;,func,main,(,),{,var,myCar,Car,=,Car,{,model,:,Toyota,,,year,:,2021,},;,var,info,string,=,myCar,.,Info,(,),;,putStringLn,(,info,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145))
        
    def test_146(self):
        self.assertTrue(TestLexer.test(
            """var a int = 1;""",
            "var,a,int,=,1,;,<EOF>",
            146
        ))
    
    def test_147(self):
        self.assertTrue(TestLexer.test(
            """0b10101; 0B11010; 0o52; 0O77;""",
            "0b10101,;,0B11010,;,0o52,;,0O77,;,<EOF>",
            147
        ))
    
    def test_148(self):
        self.assertTrue(TestLexer.test(
            """\"Hello \\"world\\" \"""",
            """Hello \\"world\\" ,<EOF>""",
            148
        ))
    
    def test_149(self):
        self.assertTrue(TestLexer.test(
            """if (x >= 10 && y <= 5 || z != 0) { return; }""",
            "if,(,x,>=,10,&&,y,<=,5,||,z,!=,0,),{,return,;,},<EOF>",
            149
        ))
    
    def test_150(self):
        self.assertTrue(TestLexer.test(
            """// This is a single-line comment\nvar x int = 5;""",
            "var,x,int,=,5,;,<EOF>",
            150
        ))
    
    def test_151(self):
        self.assertTrue(TestLexer.test(
            """/* This is a \n multi-line comment */ var y float = 3.14;""",
            "var,y,float,=,3.14,;,<EOF>",
            151
        ))
    
    def test_152(self):
        self.assertTrue(TestLexer.test(
            """for i := 0; i < 10; i += 1 { putIntLn(i); }""",
            "for,i,:=,0,;,i,<,10,;,i,+=,1,{,putIntLn,(,i,),;,},<EOF>",
            152
        ))
    
    def test_153(self):
        self.assertTrue(TestLexer.test(
            """type Point struct { x int; y int; }""",
            "type,Point,struct,{,x,int,;,y,int,;,},<EOF>",
            153
        ))
    
    def test_154(self):
        self.assertTrue(TestLexer.test(
            """const PI float = 3.14159;""",
            "const,PI,float,=,3.14159,;,<EOF>",
            154
        ))
    
    def test_155(self):
        self.assertTrue(TestLexer.test(
            """getStringLn();""",
            "getStringLn,(,),;,<EOF>",
            155
        ))

    def test_156(self):
        self.assertTrue(TestLexer.test(
            """x := 42 + 0x2A;""",
            "x,:=,42,+,0x2A,;,<EOF>",
            156
        ))
    
    def test_157(self):
        self.assertTrue(TestLexer.test(
            """var flag boolean = true && !false;""",
            "var,flag,boolean,=,true,&&,!,false,;,<EOF>",
            157
        ))
    
    def test_158(self):
        self.assertTrue(TestLexer.test(
            """\"This is a string with \\n newline\"""",
            """This is a string with \\n newline,<EOF>""",
            158
        ))
    
    def test_159(self):
        self.assertTrue(TestLexer.test(
            """func add(a int, b int) int { return a + b; }""",
            "func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>",
            159
        ))
    
    def test_160(self):
        self.assertTrue(TestLexer.test(
            """var arr [3]float = [3]float{1.1, 2.2, 3.3};""",
            "var,arr,[,3,],float,=,[,3,],float,{,1.1,,,2.2,,,3.3,},;,<EOF>",
            160
        ))
    
    def test_161(self):
        self.assertTrue(TestLexer.test(
            """/* Nested /* comment */ still valid */""",
            "<EOF>",
            161
        ))
    
    def test_162(self):
        self.assertTrue(TestLexer.test(
            """const MAX_VALUE = 100;""",
            "const,MAX_VALUE,=,100,;,<EOF>",
            162
        ))
    
    def test_163(self):
        self.assertTrue(TestLexer.test(
            """range array { putInt(i); }""",
            "range,array,{,putInt,(,i,),;,},<EOF>",
            163
        ))
    
    def test_164(self):
        self.assertTrue(TestLexer.test(
            """nil;""",
            "nil,;,<EOF>",
            164
        ))
    
    def test_165(self):
        self.assertTrue(TestLexer.test(
            """putStringLn("Hello, \\"MiniGo\\"!");""",
            """putStringLn,(,Hello, \\"MiniGo\\"!,),;,<EOF>""",
            165
        ))
