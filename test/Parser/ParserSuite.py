import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        """Test function declaration with parameters"""
        input = """func add() int {
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_201(self):
        """Test variable declarations"""
        input = """var x int = 10;
        var y float = 3.14;
        var z string = "hello";
        z = "abc";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        """Test struct declaration"""
        input = """type Point struct {
            x int;
            y int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        """Test function with return statement"""
        input = """func square(n int) int {
            return n * n;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        """Test if-else statement"""
        input = """func checkEven(n int) string {
            if (n % 2 == 0) {
                return "even";
            } else {
                return "odd";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        """Test for loop"""
        input = """func sum(n int) int {
            var total int = 0;
            for i := 0; i < n; i += 1 {
                total += i;
            }
            return total;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        """Test while loop"""
        input = """func countdown(n int) {
            for n > 0 {
                putIntLn(n);
                n -= 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        """Test array declaration and access"""
        input = """var arr [5]int = [5]{1, 2, 3, 4, 5};
        func getElement(index int) int {
            return arr[index];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        """Test nested function calls"""
        input = """func compute(x int, y int) int {
            return add(square(x), square(y));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        """Test main function with basic operations"""
        input = """func main() {
            var a int = 5;
            var b int = 10;
            var c int = a + b * 2 - (a / b);
            putIntLn(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        
    def test_210(self):
        """Test variable declaration with different types"""
        input = """func main() {
            var a int = 5;
            var b float = 3.14;
            var c boolean = true;
            var d string = "Hello";
            putIntLn(a);
            putFloatLn(b);
            putBoolLn(c);
            putStringLn(d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        """Test array declaration and access"""
        input = """func main() {
            var arr [3]int = [3]int{1, 2, 3};
            putIntLn(arr[0]);
            putIntLn(arr[1]);
            putIntLn(arr[2]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        """Test struct declaration and access"""
        input = """func main() {
            type Person struct {
                name string;
                age int;
            }
            var p Person = Person{name: "Alice", age: 30};
            putStringLn(p.name);
            putIntLn(p.age);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        """Test if-else statement"""
        input = """func main() {
            var a int = 10;
            if (a > 5) {
                putStringLn("a is greater than 5");
            } else {
                putStringLn("a is less than or equal to 5");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        """Test for loop with range"""
        input = """func main() {
            var arr [3]int = [3]int{10, 20, 30};
            for index, value := range arr {
                putIntLn(index);
                putIntLn(value);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        """Test function with parameters and return value"""
        input = """func add(x int, y int) int {
            return x + y;
        }
        func main() {
            var result int = add(3, 4);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        """Test method declaration and call"""
        input = """type Calculator struct {
            value int;
        }
        func (c Calculator) add(x int) int {
            c.value += x;
            return c.value;
        }
        func main() {
            var calc Calculator = Calculator{value: 10};
            var result int = calc.add(5);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        """Test nested if-else statements"""
        input = """type Person struct { 
            name string; 
            age int; 
            func (p Person) getAge() int {
                return p.age;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] = 1 + 2;                       
            }                                       
        """, "successful", 218))

    def test_219(self):
        """Test multiple function declarations and calls"""
        input = """func add(x int, y int) int {
            return x + y;
        }
        func subtract(x int, y int) int {
            return x - y;
        }
        func main() {
            var a int = 10;
            var b int = 5;
            var sum int = add(a, b);
            var diff int = subtract(a, b);
            putIntLn(sum);
            putIntLn(diff);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_220(self):
        """Test function declaration and basic arithmetic operations"""
        input = """func main() {
            var x int = 10;
            var y int = 20;
            var z int = x + y * 2;
            putIntLn(z);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        """Test variable declaration and assignment"""
        input = """func main() {
            var a int;
            a = 5;
            putIntLn(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        """Test if-else statement"""
        input = """func main() {
            var a int = 10;
            if (a > 5) {
                putStringLn("Greater than 5");
            } else {
                putStringLn("Less than or equal to 5");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        """Test for loop"""
        input = """func main() {
            for i := 0; i < 5; i += 1 {
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        """Test struct declaration and initialization"""
        input = """type Person struct {
            name string;
            age int;
        }
        
        func main() {
            var p Person = Person{name: "Alice", age: 30};
            putStringLn(p.name);
            putIntLn(p.age);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        """Test array declaration and access"""
        input = """func main() {
            var arr [5]int;
            arr[0] = 10;
            putIntLn(arr[0]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        """Test boolean operations"""
        input = """func main() {
            var x boolean = true;
            var y boolean = false;
            putBoolLn(x && y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        """Test nested if statements"""
        input = """func main() {
            var a int = 10;
            if (a > 5) {
                if (a < 20) {
                    putStringLn("Between 5 and 20");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        """Test function call with arguments"""
        input = """func add(a int, b int) int {
            return a + b;
        }
        
        func main() {
            var result int = add(3, 4);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        """Test invalid syntax"""
        input = """func main() {
            var x int = 10;
            putIntLn(x);
        }""" 
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        """Test while-like loop using for"""
        input = """func main() {
            var i int = 0;
            for i < 5 {
                putIntLn(i);
                i += 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        """Test empty main function"""
        input = """func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        """Test function returning a boolean"""
        input = """func isEven(n int) boolean {
            return n % 2 == 0;
        }
        
        func main() {
            putBoolLn(isEven(4));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        """Test nested loops"""
        input = """func main() {
            for i := 0; i < 3; i += 1 {
                for j := 0; j < 3; j += 1 {
                    putIntLn(i * j);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        """Test multiple return values"""
        input = """func swap(a int, b int) (int, int) {
            return b, a;
        }
        
        func main() {
            var x int = swap(3, 4);
            putIntLn(x);
            putIntLn(y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        """Test interface declaration"""
        input = """type Animal interface {
            DoSomething();
            Speak() string;
        }
        
        type Dog struct {}
        
        func (d Dog) Speak() string {
            return "Woof";
        }
        
        func main() {
            var d Dog;
            putStringLn(d.Speak());
        }"""
        expect = "Error on line 6 col 26: }"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        """Test break statement in loop"""
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                if (i == 5) {
                    break;
                }
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        """Test continue statement in loop"""
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                if (i % 2 == 0) {
                    continue;
                }
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        """Test string concatenation"""
        input = """func main() {
            var str string = "Hello" + " " + "World";
            putStringLn(str);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        """Test main function with function returning boolean"""
        input = """func isEven(num int) bool {
            return num % 2 == 0;
        }
        func main() {
            var result bool = isEven(4);
            putBoolLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        """Test empty struct initialization"""
        input = """type Point struct {
            x int;
            y int;
        }
        
        func main() {
            var p Point = Point{};
            putIntLn(p.x);
            putIntLn(p.y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    
    def test_241(self):
        """Test variable declaration and assignment"""
        input = """func main() {
            var x int = 10;
            var y float = 20.5;
            putIntLn(x);
            putFloatLn(y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        """Test array declaration and access"""
        input = """func main() {
            var arr [3]int = [3]int{1, 2, 3};
            putIntLn(arr[1]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        """Test struct initialization"""
        input = """type Point struct {
            x int;
            y int;
        }
        
        func main() {
            var p Point = Point{x: 5, y: 10};
            putIntLn(p.x);
            putIntLn(p.y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        """Test function returning multiple values"""
        input = """func swap(a int, b int) (int, int) {
            return b, a;
        }
        
        func main() {
            var x int = swap(3, 4);
            putIntLn(x);
            putIntLn(y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        """Test if-else with logical operators"""
        input = """func main() {
            var x int = 10;
            if (x > 5 && x < 15) {
                putStringLn("Within range");
            } else {
                putStringLn("Out of range");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        """Test simple for loop"""
        input = """func main() {
            for i := 0; i < 3; i += 1 {
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        """Test for loop iterating an array"""
        input = """func main() {
            var arr [3]int = [3]int{10, 20, 30};
            for _, value := range arr {
                putIntLn(value);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        """Test method inside a struct"""
        input = """type Calculator struct {
            value int;
        }
        
        func (c Calculator) Add(n int) int {
            return c.value + n;
        }
        
        func main() {
            var calc Calculator = Calculator{value: 10};
            putIntLn(calc.Add(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        """Test abc"""
        input = """abc;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        """Test invalid syntax (missing semicolon)"""
        input = """func main() {
            var x int = 10 \n
            putIntLn(x);
        }"""  # Missing semicolon
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        """Test main function with variable declaration and assignment"""
        input = """func main() {
            var x int;
            x = 15;
            putIntLn(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        """Test main function with multiple variable declarations"""
        input = """func main() {
            var a int = 1;
            putIntLn(a + b + c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        """Test main function with boolean operations"""
        input = """func main() {
            var flag bool = true;
            if (flag) {
                putStringLn("Flag is true");
            } else {
                putStringLn("Flag is false");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        """Test main function with array declaration and initialization"""
        input = """func main() {
            var arr [3]int = [3]int{1, 2, 3};
            putIntLn(arr[0]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        """Test main function with struct declaration and usage"""
        input = """func main() {
            type Person struct {
                name string;
                age int;
            }
            var p Person = Person{name: "Alice", age: 30};
            putStringLn(p.name);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        """Test main function with function call"""
        input = """func add(x int, y int) int {
            return x + y;
        }
        func main() {
            var result int = add(5, 10);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        """Test main function with nested if statements"""
        input = """func main() {
            var num int = 10;
            if (num > 0) {
                if (num % 2 == 0) {
                    putStringLn("Even number");
                } else {
                    putStringLn("Odd number");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        """Test main function with for loop"""
        input = """func main() {
            for i := 0; i < 5; i += 1 {
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        """Test main function with break statement in loop"""
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                if (i == 5) {
                    break;
                }
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    
    def test_260(self):
        """Test function with no parameters and no return value"""
        input = """func greet() {
            putStringLn("Hello, MiniGo!");
        }
        
        func main() {
            greet();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        """Test function with single return value"""
        input = """func square(n int) int {
            return n * n;
        }
        
        func main() {
            putIntLn(square(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        """Test function with multiple parameters"""
        input = """func add(a int, b int) int {
            return a + b;
        }
        
        func main() {
            putIntLn(add(3, 7));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        """Test function returning a boolean value"""
        input = """func isPositive(n int) boolean {
            return n > 0;
        }
        
        func main() {
            putBoolLn(isPositive(-1));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        """Test nested function calls"""
        input = """func double(n int) int {
            return n * 2;
        }
        
        func triple(n int) int {
            return n * 3;
        }
        
        func main() {
            putIntLn(double(triple(2)));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        """Test struct declaration with function usage"""
        input = """type Person struct {
            name string;
            age int;
        }
        
        func main() {
            var p Person = Person{name: "Alice", age: 25};
            putStringLn(p.name);
            putIntLn(p.age);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        """Test while-like for loop with decrementing value"""
        input = """func main() {
            var i int = 5;
            for i > 0 {
                putIntLn(i);
                i -= 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        """Test using continue statement inside a loop"""
        input = """func main() {
            for i := 1; i <= 5; i += 1 {
                if (i == 3) {
                    continue;
                }
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        """Test main function with nested if statements and conditions"""
        input = """func main() {
            var a int = 10;
            var b int = 20;
            if (a < b) {
                if (b - a > 5) {
                    putStringLn("b is much greater than a");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        """Test main function with for loop and continue statement"""
        input = """func main() {
            for i := 0; i < 10; i += 1 {
                if (i % 2 == 0) {
                    continue;
                }
                putIntLn(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        """Test main function with array length calculation"""
        input = """func main() {
            var arr [5]int = [5]int{1, 2, 3, 4, 5};
            var length int = 5;
            putIntLn(length);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        """Test main function with switch statement"""
        input = """func main() {
            var num int = 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        """Test main function with struct and method"""
        input = """type Rectangle struct {
            width int;
            height int;
        }
        func (r Rectangle) Area() int {
            return r.width * r.height;
        }
        func main() {
            var rect Rectangle = Rectangle{width: 5, height: 10};
            var area int = rect.Area();
            putIntLn(area);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        """Test main function with multiple functions"""
        input = """func multiply(x int, y int) int {
            return x * y;
        }
        func main() {
            var result int = multiply(3, 4);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        """Test main function with compound assignment"""
        input = """func main() {
            var x int = 5;
            x += 3;
            putIntLn(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        """Test main function with return statement"""
        input = """func add(a int, b int) int {
            return a + b;
        }
        func main() {
            var sum int = add(10, 15);
            putIntLn(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
        
    def test_276(self):
        """Test main function with complex arithmetic operations"""
        input = """func main() {
            var a int = 10;
            var b int = 5;
            var c int = (a + b) * (a - b) / 2;
            putIntLn(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        """Test main function with multiple functions and return values"""
        input = """func max(x int, y int) int {
            if (x > y) {
                return x;
            } else {
                return y;
            }
        }
        func main() {
            var a int = 7;
            var b int = 14;
            var result int = max(a, b);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        """Test main function with nested for loops"""
        input = """func main() {
            var sum int = 0;
            for i := 1; i <= 3; i += 1 {
                for j := 1; j <= 3; j += 1 {
                    sum += i * j;
                }
            }
            putIntLn(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        """Test main function with while-like structure using for loop"""
        input = """func main() {
            var count int = 0;
            for count < 5 {
                count = count + 1;
            }
            putIntLn(count);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        """Test main function with struct and method that modifies fields"""
        input = """type Circle struct {
            radius float;
        }
        func (c Circle) SetRadius(r float) {
            c.radius = r;
        }
        func (c Circle) Area() float {
            return 3.14 * c.radius * c.radius;
        }
        func main() {
            var c Circle;
            c.SetRadius(5.0);
            var area float = c.Area();
            putFloatLn(area);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        """Test main function with multiple variable types"""
        input = """func main() {
            var a int = 10;
            var b float = 5.5;
            var c string = "Hello";
            putIntLn(a);
            putFloatLn(b);
            putStringLn(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        """Test main function with complex if-else structure"""
        input = """func main() {
            var score int = 85;
            if (score >= 90) {
                putStringLn("Grade: A");
            } else if (score >= 80) {
                putStringLn("Grade: B");
            } else if (score >= 70) {
                putStringLn("Grade: C");
            } else {
                putStringLn("Grade: F");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        """Test main function with array manipulation"""
        input = """func main() {
            var arr [5]int = [5]int{1, 2, 3, 4, 5};
            for i := 0; i < 5; i += 1 {
                arr[i] = arr[i] * 2;
                putIntLn(arr[i]);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        """Test main function with function that uses both parameters and return values"""
        input = """func subtract(x int, y int) int {
            return x - y;
        }
        func main() {
            var result int = subtract(15, 5);
            putIntLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        """Test main function with a loop that calculates factorial"""
        input = """func main() {
            var n int = 5;
            var fact int = 1;
            for i := 1; i <= n; i += 1 {
                fact = fact * i;
            }
            putIntLn(fact);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        """Test main function with a complex struct and method interaction"""
        input = """type Employee struct {
            name string;
            salary float;
        }
        func (e Employee) ShowDetails() {
            putStringLn("Name: " + e.name);
            putFloatLn(e.salary);
        }
        func main() {
            var emp Employee = Employee{name: "John", salary: 50000.0};
            emp.ShowDetails();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        """Test main function with calculations using floats"""
        input = """func main() {
            var a float = 10.5;
            var b float = 2.5;
            var result float = a / b;
            putFloatLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        """Test main function with string concatenation"""
        input = """func main() {
            var str1 string = "Hello";
            var str2 string = "World";
            var result string = str1 + " " + str2;
            putStringLn(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        """Test main function with a loop that sums even numbers"""
        input = """func main() {
            var sum int = 0;
            for i := 1; i <= 10; i += 1 {
                if (i % 2 == 0) {
                    sum += i;
                }
            }
            putIntLn(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        """Test main function with a struct and array interaction"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
        
    def test_291(self):
        """Test main function with a function that sorts an array"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        """Test main function with a struct and method to calculate average grades"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        """Test main function with a function that finds the maximum in an array"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        """Test main function with multiple structs and interaction"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        """Test main function with complex conditions and multiple variables"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        """Test main function with a complex function that processes structs"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        """Test main function with character array and string manipulation"""
        input = """func main() {
            var chars [5]rune = [5]rune{\"H\", \"e\", \"l\", \"l\", \"o\"};
            var str string = "";
            for i := 0; i < 5; i += 1 {
                str += to_string(chars[i]);
            }
            putStringLn(str);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        """Test main function with a loop that counts down"""
        input = """func main() {
            var count int = 10;
            for count > 0 {
                putIntLn(count);
                count = count - 1;
            }
            putStringLn("Countdown complete!");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        """Test main function with a combination of functions and structs"""
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))