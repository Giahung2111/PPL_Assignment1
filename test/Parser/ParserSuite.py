import unittest
from TestUtils import TestParser

# class ParserSuite(unittest.TestCase):

#     def test_001(self):
#         input = """/* This is a /* nested
# multi-line
# comment. */"""
#         expect = "Error on line 3 col 12: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,301))

#     def test_002(self):
#         input = """func foo () {
#         };"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,302))
    
#     def test_003(self):
#         input = """func main({};"""
#         expect = "Error on line 1 col 11: {"
#         self.assertTrue(TestParser.test(input,expect,303))
#     def test_004(self):
#         input = """var int;"""
#         expect = "Error on line 1 col 5: int"
#         self.assertTrue(TestParser.test(input,expect,304))
#     def test_005(self):
#         input = """var i ;"""
#         expect = "Error on line 1 col 7: ;"
#         self.assertTrue(TestParser.test(input,expect,305))
#     def test_006(self):
#         self.assertTrue(TestParser.test("""const k = -a + -!-!c - ---[2]int{2};""", "Error on line 1 col 17: !", 306)) # --c hay -(-c)
#     def test_007(self):     
#         input = """    
#             func Alo() {
#                 if (x > 10) { foo() }
#             } ;
#         """
#         expect = "Error on line 3 col 37: }"
#         self.assertTrue(TestParser.test(input,expect,307))
#     def test_008(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) { foo(); }
#             } 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,308))
#     def test_009(self):
#         input = """    
#             func Alo() {if (x > 10) { foo(); }} 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,309))
#     def test_010(self):
#         input = """    
#             func Alo() 
#             {
#                 if (x > 10) { foo() }
#             } 
#         """
#         expect = "Error on line 2 col 24: ;"
#         self.assertTrue(TestParser.test(input,expect,310))

#     def test_011(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) { } 
#                 if (x > 10) {

#                 } else if (x == 10) {
#                     var z str;
#                 } else {
#                     var z ID;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,311))
#     def test_012(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) { foo() }
#             } 
#         """
#         expect = "Error on line 3 col 37: }"
#         self.assertTrue(TestParser.test(input,expect,312))

#     def test_013(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) {
#                     hoho();
#                 } else if (x == 10) {
#                     var z str;
#                 };
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,313))
#     def test_014(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) {
#                     hoho();
#                 } else if (x == 10) {
#                     var z str;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,314))
#     def test_015(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) {
#                     hoho();
#                 } 
#                 else if (x == 10) {
#                     hoho();
#                 } else if (x == 11) {
#                     hohoho();
#                 };
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,315))
#     def test_016(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) {
#                     hoho();
#                 } 
#                 else if (x == 10) {
#                     hoho();
#                 } else {
#                     hohoho();
#                 };
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,316))
#     def test_017(self):
#         input = """    
#             func Alo() {
#                 if (x > 10) {
#                     hoho();
#                 } 
#                 else if (x == 10) {
#                     hoho();
#                 } 
#                 else {
#                     hohoho();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,317))
#     def test_018(self):
#         input = """    
#             func Alo() {
#                 if (x < 10) {
#                     hoho();
#                 } 
#                 else if (x == 10) {
#                     fuho();
#                 } else if (x == 11) {
#                     banveso();
#                 } else if (x == 12) {
#                     fuho();
#                 } else {
#                     banveso();
#                 };
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,318))
#     def test_019(self):
#         input = """    
#             func Alo() {
#                 if (x < 10) {
#                     hoho();
#                 } 
#                 else if (x == 10) {
#                     fuho();
#                 } else if (x == 11) {
#                     banveso();
#                 } else if (x == 12) {
#                     fuho();
#                 } else {
#                     banveso();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,319))




#     def test_020(self):
#         input = """ 
#         func Alo() {   
#             for i < 10 {}
#                 for i := 0; i < 10; i += 1 {}
#                 for index, value := range array {}
#         }
#         """
#         expect = "Error on line 4 col 23: :="
#         self.assertTrue(TestParser.test(input,expect,320))

#     def test_021(self):
#         input = """ 
#         func Alo() {   
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,321))
#     def test_022(self):
#         input = """    
#             func Alo() {
#                 for i := 0; 
#                     i < 10; 
#                     i += 1 {
#                     }
#             }
#         """
#         expect = "Error on line 3 col 23: :="
#         self.assertTrue(TestParser.test(input,expect,322))
#     def test_023(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,323))
#     def test_024(self):
#         input = """    
#             func Alo() {     



#                 for i < 10
#                 {
                 
                
#                 }



                
#             }
#         """
#         expect = "Error on line 7 col 17: {"
#         self.assertTrue(TestParser.test(input,expect,324))
#     def test_025(self):
#         input = """    
#             func Alo() { for i < 10 {fu();} }
#         """
#         expect = "Error on line 2 col 45: }"
#         self.assertTrue(TestParser.test(input,expect,325))
#     def test_026(self):
#         input = """    
#             func Alo() {
#                 for i, j := 0, 10; i < 10 && j > 0; i += 1, j -= 1 {
#                     putInt(i + j);
#                 };
#             }
#         """
#         expect = "Error on line 3 col 29: 0"
#         self.assertTrue(TestParser.test(input,expect,326))
#     def test_027(self):
#         input = """    
#             func Alo() {
#                 for i := 0; i += 1 {}
#             }
#         """
#         expect = "Error on line 3 col 23: :="
#         self.assertTrue(TestParser.test(input,expect,327))
#     def test_028(self):
#         input = """    
#             func Alo() {
#                 for i < 10; i += 1 {}
#             }
#         """
#         expect = "Error on line 3 col 31: +="
#         self.assertTrue(TestParser.test(input,expect,328))


#     def test_029(self):
#         input = """    
#             func Alo() {
#                 for index, 
#                     value := Range array {}
#             }
#         """
#         expect = "Error on line 4 col 30: Range"
#         self.assertTrue(TestParser.test(input,expect,329))
#     def test_030(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             };
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,330))
#     def test_031(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,331))
#     def test_032(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             };
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,332))
#     def test_033(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,333))
#     def test_034(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             };
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,334))
#     def test_035(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,335))
#     def test_036(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             };
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,336))
#     def test_037(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,337))
#     def test_038(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             };
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,338))
#     def test_039(self):
#         input = """    
#             for index, value := range [3]int{1,2,3} {
#                 foo();
#             }
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,339))



#     def test_040(self):
#         input = """    
#             var matrix [3][4]int;
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,340))
#     def test_041(self):
#         input = input = """
#             var matrix [2][3][4]int = {
#                 {
#                     {1, 2, 3, 4}, 
#                     {5, 6, 7, 8}, 
#                     {9, 10, 11, 12}
#                 }, 
#                 {
#                     {13, 14, 15, 16}, 
#                     {17, 18, 19, 20}, 
#                     {21, 22, 23, 24}
#                 }
#             };
#         """
#         expect = "Error on line 2 col 39: {"
#         self.assertTrue(TestParser.test(input,expect,341))
#     def test_042(self):
#         input = """    
#             x := matrix[1][2];
#         """
#         expect = "Error on line 2 col 13: x"
#         self.assertTrue(TestParser.test(input,expect,342))
#     def test_043(self):
#         input = """    
#             matrix[0][1] = 42;
#         """
#         expect = "Error on line 2 col 13: matrix"
#         self.assertTrue(TestParser.test(input,expect,343))
#     def test_044(self):
#         input = """    
#             for i := 0; i < 2; i += 1 {
#                 for j := 0; j < 3; j += 1 {
#                     alo(matrix[i][j])
#                 }
#             };
#         """
#         expect = "Error on line 2 col 13: for"
#         self.assertTrue(TestParser.test(input,expect,344))
#     def test_045(self):
#         input = """    
#             const a = [5]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil, [1]int{1}}
#         """
#         expect = "Error on line 2 col 43: }"
#         self.assertTrue(TestParser.test(input,expect,345))
#     def test_046(self):
#         input = """    
#             var alo int = b[1].d.[3].(a).foo().1[1].1.-1.true.flase.nil.[1]int{1}."alo1234" 
#         """
#         expect = "Error on line 2 col 37: ."
#         self.assertTrue(TestParser.test(input,expect,346))
#     def test_047(self):
#         input = """    
#             var a = [3]int{1,2,3};
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,347))
#     def test_048(self):
#         input = """    
#             var a [33]float = {13,45,25};
#         """
#         expect = "Error on line 2 col 31: {"
#         self.assertTrue(TestParser.test(input,expect,348))
#     def test_049(self):
#         input = """    
#             arr := [2][2]int{{{{{{0}}}}}} 
#         """
#         expect = "Error on line 2 col 13: arr"
#         self.assertTrue(TestParser.test(input,expect,349))





#     def test_050(self):
#         input = """    
#             func Alo() {
#                 arr := [2][2]int{{2,3}} 
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,350))
#     def test_051(self):
#         input = """    
#             func Alo() 
#             {
#             x = foo()
#             return x + hoo() }
#         """
#         expect = "Error on line 2 col 24: ;"
#         self.assertTrue(TestParser.test(input,expect,351))
#     def test_052(self):
#         input = """    
#             func Alo() {
#             x = foo()
#             return x + hoo() } 
#         """
#         expect = "Error on line 4 col 30: }"
#         self.assertTrue(TestParser.test(input,expect,352))
#     def test_053(self):
#         input = """    
#             func Alo() {
#             x = foo();return x+hoo()} 
#         """
#         expect = "Error on line 3 col 37: }"
#         self.assertTrue(TestParser.test(input,expect,353))
#     def test_054(self):
#         input = """    
#             func Alo() {
#             x = foo();return x+hoo();}
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,354))
#     def test_055(self):
#         input = """    
#             func Alo() {
#             const x = 1;
#             return x+=1+=1+=1+=1+=1;
#             }
#         """
#         expect = "Error on line 4 col 21: +="
#         self.assertTrue(TestParser.test(input,expect,355))
#     def test_056(self):
#         input = """    
#             func Alo() {
#             x = foo()
#             return x + hoo() 
#             }"""
#         expect = "Error on line 5 col 14: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,356))
#     def test_057(self):
#         input = """    
#             var putInt = 1.1.1.1
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,357))
#     def test_058(self):
#         input = """    
#             var getString =   1 
#                             + 2 
#                             + 3
#         """
#         expect = "Error on line 3 col 29: +"
#         self.assertTrue(TestParser.test(input,expect,358))
#     def test_059(self):
#         input = """    
#             var putStringLn = 1 +
#                               2 +
#                               3  
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,359))


#     def test_060(self):
#         input = """    
#             func Alo(); 
#             {x = foo();return x+hoo();}
#         """
#         expect = "Error on line 2 col 23: ;"
#         self.assertTrue(TestParser.test(input,expect,360))
#     def test_061(self):
#         input = """    
#             func Add() {
#                 if (x.foo().b[2]) 
#                 {
#                     if (){}
#                 } 
#             }"""
#         expect = "Error on line 3 col 35: ;"
#         self.assertTrue(TestParser.test(input,expect,361))
#     def test_062(self):
#         input = """
#             func Add() {
#                 for const i = 0; i < 10; i += 1 {
#                     // loop body
#                 }
#             }"""
#         expect = "Error on line 3 col 21: const"
#         self.assertTrue(TestParser.test(input,expect,362))
#     def test_063(self):
#         input = """ func main () {
#                         arr :=[2][3]int{
#                         {1,2,3}, 
#                         {3,4.5}};
#                     }"""
#         expect = "Error on line 5 col 22: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,363))
#     def test_064(self):
#         input = """ func main () {
#                         arr :=[2][3]int{
#                         {1,2}, 
#                         {3,4}
#                         };
#                     }"""
#         expect = "Error on line 4 col 30: ;"
#         self.assertTrue(TestParser.test(input,expect,364))
#     def test_065(self):
#         input = """    
#             var a  = [1]int{4} + 2; 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,365))
#     def test_066(self):
#         input = """ func Alo(){   
#             var multi arr [0xA][0o5]int
#             }
#         """
#         expect = "Error on line 2 col 27: ["
#         self.assertTrue(TestParser.test(input,expect,366))
#     def test_067(self):
#         input = """ func Alo(){   
#             a[2+1][3+a] := b[2+=1] + 1;
#             }
#         """
#         expect = "Error on line 2 col 21: +"
#         self.assertTrue(TestParser.test(input,expect,367))
#     def test_068(self):
#         input = """  func Alo(){  
#             a[2+1][3+a] := b[!1] + 1;
#             }
#         """
#         expect = "Error on line 2 col 21: +"
#         self.assertTrue(TestParser.test(input,expect,368))
#     def test_069(self):
#         input = """ func Alo(){    
#             var multi arr [a][1]int
#             }
#         """
#         expect = "Error on line 2 col 27: ["
#         self.assertTrue(TestParser.test(input,expect,369))
#     def test_070(self):
#         input = """    
#             var multi arr [a][1+1]int
#         """
#         expect = "Error on line 2 col 27: ["
#         self.assertTrue(TestParser.test(input,expect,370))
#     def test_071(self):
#         input = """    
#             var multi arr [nil][1]int
#         """
#         expect = "Error on line 2 col 27: ["
#         self.assertTrue(TestParser.test(input,expect,371))
#     def test_072(self):
#         input = """func Alo(){     
#             a[nil][ID{}] := b[foo()] + 1;
#             }
#         """
#         expect = "Error on line 2 col 20: ID"
#         self.assertTrue(TestParser.test(input,expect,372))
#     def test_073(self):
#         input = """    
#             type alo interface {

#             add()

#             }"""
#         expect = "Error on line 6 col 14: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,373))
#     def test_074(self):
#         input = """    
#             var putLn = 1 + 2 + 3
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,374))
#     def test_075(self):
#         input = """    
#             func Alo(x int, y int) int {return;}
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,375))
#     def test_076(self):
#         input = """
#                 func Add() {
#                     a.foo() += 2;       
#                 }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,376))
#     def test_077(self):# trg
#         input = """    
#             type Person struct {
#                 name string ;
#                 age int ;   
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,377))
#     def test_078(self):# trg
#         input = """    
#             type Person struct {
#                 name string ;
#                 age int ;   
#             }
#             p := Person{name: "Alice", age: 30}
#         """
#         expect = "Error on line 6 col 13: p"
#         self.assertTrue(TestParser.test(input,expect,378))
#     def test_079(self):# trg
#         input = """func main() {    
#             PutStringLn(p.name) // Output: Alice
#             PutIntLn(p.age) // Output: 30
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,379))
#     def test_080(self):
#         input = """    
#             type Person struct {}
#         """
#         expect = "Error on line 2 col 33: }"
#         self.assertTrue(TestParser.test(input,expect,380))
#     def test_081(self):
#         input = """    
#             var z ALO = [2]int{};
#         """
#         expect = "Error on line 2 col 32: }"
#         self.assertTrue(TestParser.test(input,expect,381))
#     def test_082(self):
#         input = """    
#             func (c c) Add(x int) {};
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,382))
#     def test_083(self):
#         input = """    
#             func (c c)
#               Add(x int)
#                 {
#                 };
#         """
#         expect = "Error on line 2 col 23: ;"
#         self.assertTrue(TestParser.test(input,expect,383))
#     def test_084(self):
#         input = """    
#             func (c c) Add(x int) {
#             foo();
#             };
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,384))
#     def test_085(self):
#         input = """    
#             func (c c) Add(x int) {
#             foo()};
#         """
#         expect = "Error on line 3 col 18: }"
#         self.assertTrue(TestParser.test(input,expect,385))
#     def test_086(self):
#         input = """    
#             var a = a.foo()[2];
#         """
#         expect = "Error on line 2 col 31: ;"
#         self.assertTrue(TestParser.test(input,expect,386))
#     def test_087(self):
#         input = """    
#             var c [2][3]ID = [2][3]ID{{1,2,3},{4,5,6}};
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,387))
#     def test_088(self):
#         input = """    
#             var c [2][3]ID
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,388))
#     def test_089(self):
#         input = """    
#             var putLn = nil
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,389))
#     def test_090(self):# trg
#         input = """    
#             func (p Person) Greet() string {
#                 return "Hello, " + p.name
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,390))
#     def test_091(self):# trg
#         input = """    
#             type Calculator interface {
#                 Add(x, y int) int;
#                 Subtract(a, b float, c int) float;
#                 Reset()
#                 SayHello(name string)
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,391))
#     def test_092(self):# trg
#         input = """    
#             type Calculator struct {
#                 value int;
#             }
#             func (c Calculator) Add(x int) int {
#                 c.value += x;
#                 return c.value;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,392))
#     def test_093(self):
#         input = """    
#             func (p Person) Greet() string {
#                 for index, value := range STRUCT{}{
#                     // loop body                                   
#                 };
#             };  
#         """
#         expect = "Error on line 3 col 51: {"
#         self.assertTrue(TestParser.test(input,expect,393))
#     def test_094(self):#trg
#         input = """func Alo(){     
#             arr := [3]int{10, 20, 30}
#             marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,394))
#     def test_095(self):
#         input = """
#         func Alo(){     
#             if (x > 10) {
#                 println("x is greater than 10");
#             } else if (x == 10) {
#                 println("x is equal to 10");
#             } else {
#                 println("x is less than 10");
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,395))
#     def test_096(self):#trg
#         input = """func Alo(){     
#             arr := [3]int{10, 20, 30}
#             for _, value := range arr {
#                 // value: 10, 20, 30
#             }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,396))
#     def test_097(self):#trg
#         input = """func Alo(){     
#                 arr := [3]int{10, 20, 30}
#                 for index, value := range arr {
#                     // index: 0, 1, 2
#                     // value: 10, 20, 30
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,397))
#     def test_098(self):
#         input = """func Alo(){    
#             str1 := "Hello"
#             str2 := "World"
#             str3 := str1 + " " + str2 // str3 == "Hello World"
#             str4 := "apple"
#             str5 := "banana"
#             result := str4 == str5 // result == false
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,398))
#     def test_099(self):
#         input = """var y = "Hello\\r\\n"; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,399))
#     def test_100(self):
#         input = """var y = "Hello\r\n"; """
#         expect = "Hello"
#         self.assertTrue(TestParser.test(input,expect,400))
#     def test_101(self):
#         input = """const a = [1]int{[1]int{1}};"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,401))

#     def test_102(self):
#         self.assertTrue(TestParser.test("""func Add() {
#                                         return (arr[2]).b
#                                         return (1).c
#                                                };""", "successful", 402))
#     def test_103(self):
#         self.assertTrue(TestParser.test("""func Add() {// alo
#                                                }// alo
#                                                """, "successful", 403))
class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1;", "successful", 1))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;", "successful", 2))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};", "successful", 3))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};", "Error on line 1 col 16: 1.", 4))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};", "successful", 5))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;", "successful", 6))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;", "successful", 7))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];", "successful", 8))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();", "successful", 9))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        """, "successful", 10))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const VoTien = a.b() + 2;
        """, "successful", 11))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        """, "successful", 12))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        """, "successful", 13))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        """, "successful", 14))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {}                                                                       
        """, "Error on line 2 col 32: }", 15))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                                                
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                                
                SayHello(name string);
                                                
            }
            type VoTien interface {}                                                                       
        """, "Error on line 11 col 35: }", 16))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                            
                const VoTien = a.b() + 2;
            }                                       
        """, "successful", 17))

    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        """, "successful", 18))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        """, "successful", 19))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        """, "successful", 20))

    def test_021(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const a = 0b11;                         
        """, "successful", 21))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [true]int{1};                         
        """, "Error on line 2 col 28: true", 25))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {};                         
        """, "successful", 31))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        """, "successful", 32))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        """, "successful", 36))

    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        """, "successful", 37))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        """, "successful", 45))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = foo().a[2].goo();                         
        """, "successful", 50))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var c [2][3]ID
        """, "successful", 64))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            const a =;
        """, "Error on line 2 col 21: ;", 67))

    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(x int, y [2]int) [2]id {return ;}
        """, "successful", 69))
