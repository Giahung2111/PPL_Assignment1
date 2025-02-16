"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1;","successful", 1))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;","successful", 2))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", 3))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", 4))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", 5))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", 6))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", 7))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", 8))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", 9))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", 10))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const VoTien = a.b() + 2;
        ""","successful", 11))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", 12))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", 13))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", 14))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {}                                                                       
        ""","Error on line 2 col 32: }", 15))

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
        ""","Error on line 11 col 35: }", 16))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", 17))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", 18))

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
        ""","successful", 19))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", 20))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", 21))
       
    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const a = 0b11;                         
        ""","successful", 22))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const a = 1.;                         
        ""","successful", 23))

    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN 1;                         
        ""","Error on line 2 col 25: 1", 24))
    
    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = int{1};                         
        ""","Error on line 2 col 27: int", 25))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 28: true", 26))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 28: ]", 27))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 28: ]", 28))

    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [2]int{1;                         
        ""","Error on line 2 col 35: ;", 29))
    
    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [2]int{1,3,4;                         
        ""","Error on line 2 col 39: ;", 30))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 34: }", 31))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {};                         
        ""","successful", 32))

    def test_033(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", 33))

    def test_034(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = int {};                         
        ""","Error on line 2 col 27: int", 34))

    def test_035(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID + 3;                         
        ""","successful", 35))
    
    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {a: };                         
        ""","Error on line 2 col 34: }", 36))

    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", 37))
    
    def test_038(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", 38))

    def test_039(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a + b - [2]int{2} + c - z;                         
        ""","successful", 39))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a * b / d % e * 2;                         
        ""","successful", 40))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        ""","successful", 41))

    def test_042(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", 42))

    def test_043(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 30: ,", 43))

    def test_044(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[];                         
        ""","Error on line 2 col 29: ]", 44))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].foo();                         
        ""","successful", 45))

    def test_046(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        ""","successful", 46))

    def test_047(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        ""","successful", 47))

    def test_048(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1,);                         
        ""","Error on line 2 col 47: )", 48))

    def test_049(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;                         
        ""","successful", 49))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
        ""","successful", 50))

    def test_051(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = foo().a[2].goo();                         
        ""","successful", 51))

    def test_052(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k = [2]int{1}[3][4].foo();                         
        ""","successful", 52))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
        ""","successful", 53))

    def test_054(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", 54))

    def test_055(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k = foo() + foo(a{a:2}) + foo(2, 3,4);                         
        ""","successful", 55))

    def test_056(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k =  int;                         
        ""","Error on line 2 col 23: int", 56))

    def test_057(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k =  (1, 2);                         
        ""","Error on line 2 col 25: ,", 57))

    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a VOTIEN = 2 + 3 / 4;
        ""","successful", 58))

    def test_059(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", 59))

    def test_060(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a [][3]int = 2 + 3 / 4;
        ""","Error on line 2 col 19: ]", 60))

    def test_061(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a = a.foo()[2];
        ""","successful", 61))

    def test_062(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a = ;
        ""","Error on line 2 col 20: ;", 62))

    def test_063(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var a 1;
        ""","Error on line 2 col 18: 1", 63))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var c [2][3]int;
        ""","successful", 64))

    def test_065(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var c [2][3]ID
        ""","successful", 65))

    def test_066(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            const a;
        ""","Error on line 2 col 19: ;", 66))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            const a := 1 + foo.a[2];
        ""","Error on line 2 col 20: :=", 67))

    def test_068(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            const a =;
        ""","Error on line 2 col 21: ;", 68))

    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            
            var a int; var d = 2;
                                        
            var d = 2;
                                        
            const a = 2; var d int = 3;
                                        
            
            var d = 2;""","successful", 69))
        
    def test_070(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", 70))
        
    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add() [2]id {return ;}
""","successful", 71))
        
    def test_072(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(a) [2]id {return ;}
""","Error on line 2 col 22: )", 72))
        
    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(int a) int {return ;}
""","Error on line 2 col 21: int", 73))
        
    def test_074(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add() {return ;}
""","successful", 74))
        
    def test_075(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(a int, ) {}
""","Error on line 2 col 28: )", 75))
        
    def test_076(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {value int}
""","Error on line 2 col 45: }", 76))
        
    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {value int;}
""","successful", 77))
        
    def test_078(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", 78))
        
    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 22: a", 79))
        
    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 22: =", 80))
        
    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", 81))
        
    def test_082(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 46: }", 82))
        
    def test_083(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset()
        }
""","successful", 83))
        
    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset();}
""","successful", 84))
        
    def test_085(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", 85))
        
    def test_086(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x int,c,d ID){}
        }
""","Error on line 3 col 33: {", 86))
        
    def test_087(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset();} type Person struct{value int;}
""","Error on line 2 col 49: type", 87))
        
    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset();}; type Person struct{value int;}
""","successful", 88))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(x int, y int) int  {return ;};
""","successful", 89))
        
    def test_090(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) Add(x int) int {return ;}
""","successful", 90))
        
    def test_091(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 20: int", 91))
        
    def test_092(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x int) {return ;}
""","successful", 92))
        
    def test_093(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {return ;}
""","successful", 93))
        
    def test_094(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c [2]c) Add(x int) {return ;}
""","Error on line 2 col 20: [", 94))
        
    def test_095(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (int c) Add(x int) {return ;}
""","Error on line 2 col 18: int", 95))
        
    def test_096(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x int) {return ;};
""","successful", 96))
        
    def test_097(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
            func (c c) Add(x int) {return ;}
                                        
            func Add(x int) {return ;}; var c int;
                                        
            var c int; type Calculator struct{c int;}; type Calculator struct{c int;} var c int;
""","Error on line 7 col 86: var", 97))
        
    def test_098(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
            var c int func (c c) Add(x int) {return ;}
""","Error on line 3 col 22: func", 98))
        
    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
            const a = 2 func (c c) Add(x int) {return ;}
""","Error on line 3 col 24: func", 99))
        
    def test_100(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
            const MaxSize = 100 + 50; func (c c) Add() {return ;}
""","successful", 100))
        
    def test_101(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
                                        
""","Error on line 3 col 0: <EOF>", 101))
        
    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Add() {
                                        }
""","successful", 102))
        
    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a int = 2;      
                                    };""","successful", 103))

    def test_104(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a int;      
                                    };""","successful", 104))
        
    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""","successful", 105))
        
    def test_106(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         const a = a[2].b;      
                                    };""","successful", 106))
        
    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    };""","successful", 107))
        
    def test_108(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b var a = "s";           
                                    };""","Error on line 4 col 55: var", 108))

    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""","successful", 109))
        

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2].b := 2;       
                                    };""","successful", 110))
        

    def test_111(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""","successful", 111))

    def test_112(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""","Error on line 3 col 48: +=", 112))

    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        2 + 2 += 2;       
                                    };""","Error on line 3 col 40: 2", 113))
        
    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       ID {id:2}.c += 2;       
                                    };""","Error on line 3 col 42: {", 114))
        
    def test_115(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""","successful", 115))
        
    def test_116(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""","successful", 116))
        
    def test_117(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){return;}
                                        } 
                                    };""","Error on line 4 col 48: )", 117))
        
    def test_118(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };""","successful", 118))
        
    def test_119(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {return
                                        } else if(){
                                        }
                                    };""","Error on line 4 col 50: )", 119))
        
    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {return; 
                                        } else if(1){return; 
                                        }else if(1){return; 
                                        }else if(2){return
                                        }else {return; 
                                        }
                                    };""","successful", 120))
        
    def test_121(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for true {return; }
                                    };""","successful", 121))
        
    def test_122(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", 122))
        
    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", 123))
        
    def test_124(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", 124))
        
    def test_125(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", 125))
        
    def test_126(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", 126))
        
    def test_127(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 44: const", 127))
        
    def test_128(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: [", 128))
        
    def test_129(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return; 
                                        }
                                    };""","Error on line 3 col 76: {", 129))
        
    def test_130(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); var i [2]int = 0 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 75: var", 130))
        
    def test_131(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","successful", 131))
        
    def test_132(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 52: ,", 132))
        
    def test_133(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index.ab, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 52: ,", 133))
        
    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value[2] := range arr {
                                        // index: 0, 1, 2
                                        return; 
                                        }
                                    };""","Error on line 3 col 56: [", 134))
        
    def test_135(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range arr[2] {return
                                        }
                                    };""","successful", 135))
        
    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""","successful", 136))
        
    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range 23 {
                                            for index, value := range 23 {return; }
                                        }
                                    };""","successful", 137))
        
    def test_138(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", 138))
        
    def test_139(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", 139))
        
    def test_140(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return return 2 + a[2].b()
                    
                                    };""","Error on line 3 col 47: return", 140))
        
    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break continue
                    
                                    };""","Error on line 3 col 46: continue", 141))
        
    def test_142(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo();
                                        foo()
                                    };""","successful", 142))
        
    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", 143))
        
    def test_144(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""","Error on line 3 col 40: (", 144))
        
    def test_145(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", 145))
        
    def test_146(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        {break;}
                                    };""","Error on line 3 col 40: {", 146))
        
    def test_147(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                        break;
                                    func Add() {
                                    };""","Error on line 2 col 40: break", 147))
        
    def test_148(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    };""","Error on line 4 col 50: c", 148))
        
    def test_149(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return (2 + 3)[b]
                                        return -1.c[c]
                                    };""","Error on line 4 col 50: c", 149))
        
    def test_150(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (1) {return struct;}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    };""","Error on line 3 col 55: struct", 150))
        
    def test_151(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}
                                    };""","Error on line 3 col 75: string", 151))
        
    def test_152(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}else  {return struct;}
                                    };""","Error on line 3 col 75: string", 152))
        
    def test_153(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{1+1}                    
""","Error on line 1 col 18: +", 153))
        
    def test_154(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", 154))
        
    def test_155(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{}                    
""","Error on line 1 col 17: }", 155))
        
    def test_156(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", 156))
        
    def test_157(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
""","successful", 157))
        
    def test_158(self):
        self.assertTrue(TestParser.test("""
        func Add(x, y int, b float) {return ;}           
""","successful", 158))
        
    def test_159(self):
        self.assertTrue(TestParser.test("""
        func (c c) Add(x, y int, b float) {return ;}           
""","successful", 159))
        
    def test_160(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }      
""","successful", 160))
        
    def test_161(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            c int  c int;                                                    
        }      
""","Error on line 3 col 19: c", 161))
        
    def test_162(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""","Error on line 10 col 27: ;", 162))