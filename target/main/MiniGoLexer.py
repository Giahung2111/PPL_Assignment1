# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u023b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\7\67\u0170\n\67\f\67\16\67\u0173\13\67\38\3")
        buf.write("8\38\78\u0178\n8\f8\168\u017b\138\58\u017d\n8\39\39\3")
        buf.write("9\69\u0182\n9\r9\169\u0183\39\39\3:\3:\3:\6:\u018b\n:")
        buf.write("\r:\16:\u018c\3:\3:\3;\3;\3;\6;\u0194\n;\r;\16;\u0195")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\5?\u01a2\n?\3?\3?\3?\7")
        buf.write("?\u01a7\n?\f?\16?\u01aa\13?\5?\u01ac\n?\3@\3@\3@\7@\u01b1")
        buf.write("\n@\f@\16@\u01b4\13@\3@\5@\u01b7\n@\3@\3@\6@\u01bb\n@")
        buf.write("\r@\16@\u01bc\3@\5@\u01c0\n@\3@\6@\u01c3\n@\r@\16@\u01c4")
        buf.write("\3@\5@\u01c8\n@\3A\3A\3A\7A\u01cd\nA\fA\16A\u01d0\13A")
        buf.write("\5A\u01d2\nA\3B\3B\3B\3B\3B\3B\7B\u01da\nB\fB\16B\u01dd")
        buf.write("\13B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u01eb\nC\3")
        buf.write("D\3D\3D\3D\3E\3E\3E\3E\7E\u01f5\nE\fE\16E\u01f8\13E\3")
        buf.write("E\3E\3F\3F\3F\3F\3F\7F\u0201\nF\fF\16F\u0204\13F\3F\3")
        buf.write("F\3F\3F\3F\3G\6G\u020c\nG\rG\16G\u020d\3G\3G\3H\3H\3H")
        buf.write("\3I\3I\3I\3I\3I\3I\7I\u021b\nI\fI\16I\u021e\13I\3I\5I")
        buf.write("\u0221\nI\3I\3I\3J\3J\3K\3K\3K\3K\3K\3K\7K\u022d\nK\f")
        buf.write("K\16K\u0230\13K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3\u0202")
        buf.write("\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w\2y\2{\2}\2\177=\u0081\2\u0083>\u0085?\u0087@\u0089")
        buf.write("A\u008bB\u008dC\u008fD\u0091E\u0093F\u0095G\u0097H\3\2")
        buf.write("\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd")
        buf.write("\4\2QQqq\4\2ZZzz\5\2\62;CHch\3\2\629\3\2\62\63\4\2GGg")
        buf.write("g\4\2--//\5\2\f\f$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2")
        buf.write("\13\f\16\17\"\"\3\3\f\f\7\2))^^ppttvv\2\u0255\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099")
        buf.write("\3\2\2\2\5\u009b\3\2\2\2\7\u009e\3\2\2\2\t\u00a3\3\2\2")
        buf.write("\2\13\u00a7\3\2\2\2\r\u00ae\3\2\2\2\17\u00b3\3\2\2\2\21")
        buf.write("\u00b8\3\2\2\2\23\u00bf\3\2\2\2\25\u00c9\3\2\2\2\27\u00d0")
        buf.write("\3\2\2\2\31\u00d4\3\2\2\2\33\u00da\3\2\2\2\35\u00e2\3")
        buf.write("\2\2\2\37\u00e8\3\2\2\2!\u00ec\3\2\2\2#\u00f5\3\2\2\2")
        buf.write("%\u00fb\3\2\2\2\'\u0101\3\2\2\2)\u0105\3\2\2\2+\u010a")
        buf.write("\3\2\2\2-\u0110\3\2\2\2/\u011c\3\2\2\2\61\u0125\3\2\2")
        buf.write("\2\63\u0127\3\2\2\2\65\u0129\3\2\2\2\67\u012b\3\2\2\2")
        buf.write("9\u012d\3\2\2\2;\u012f\3\2\2\2=\u0132\3\2\2\2?\u0135\3")
        buf.write("\2\2\2A\u0138\3\2\2\2C\u013b\3\2\2\2E\u013d\3\2\2\2G\u013f")
        buf.write("\3\2\2\2I\u0142\3\2\2\2K\u0145\3\2\2\2M\u0147\3\2\2\2")
        buf.write("O\u014a\3\2\2\2Q\u014d\3\2\2\2S\u0150\3\2\2\2U\u0153\3")
        buf.write("\2\2\2W\u0156\3\2\2\2Y\u0159\3\2\2\2[\u015b\3\2\2\2]\u015d")
        buf.write("\3\2\2\2_\u015f\3\2\2\2a\u0161\3\2\2\2c\u0163\3\2\2\2")
        buf.write("e\u0165\3\2\2\2g\u0167\3\2\2\2i\u0169\3\2\2\2k\u016b\3")
        buf.write("\2\2\2m\u016d\3\2\2\2o\u017c\3\2\2\2q\u017e\3\2\2\2s\u0187")
        buf.write("\3\2\2\2u\u0190\3\2\2\2w\u0199\3\2\2\2y\u019b\3\2\2\2")
        buf.write("{\u019d\3\2\2\2}\u019f\3\2\2\2\177\u01c7\3\2\2\2\u0081")
        buf.write("\u01d1\3\2\2\2\u0083\u01d3\3\2\2\2\u0085\u01ea\3\2\2\2")
        buf.write("\u0087\u01ec\3\2\2\2\u0089\u01f0\3\2\2\2\u008b\u01fb\3")
        buf.write("\2\2\2\u008d\u020b\3\2\2\2\u008f\u0211\3\2\2\2\u0091\u0214")
        buf.write("\3\2\2\2\u0093\u0224\3\2\2\2\u0095\u0226\3\2\2\2\u0097")
        buf.write("\u0235\3\2\2\2\u0099\u009a\7<\2\2\u009a\4\3\2\2\2\u009b")
        buf.write("\u009c\7k\2\2\u009c\u009d\7h\2\2\u009d\6\3\2\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1")
        buf.write("\u00a2\7g\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4")
        buf.write("\u00a5\7q\2\2\u00a5\u00a6\7t\2\2\u00a6\n\3\2\2\2\u00a7")
        buf.write("\u00a8\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7v\2\2\u00aa")
        buf.write("\u00ab\7w\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7p\2\2\u00ad")
        buf.write("\f\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7w\2\2\u00b0")
        buf.write("\u00b1\7p\2\2\u00b1\u00b2\7e\2\2\u00b2\16\3\2\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7{\2\2\u00b5\u00b6\7r\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\20\3\2\2\2\u00b8\u00b9\7u\2\2\u00b9")
        buf.write("\u00ba\7v\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7w\2\2\u00bc")
        buf.write("\u00bd\7e\2\2\u00bd\u00be\7v\2\2\u00be\22\3\2\2\2\u00bf")
        buf.write("\u00c0\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7h\2\2\u00c5")
        buf.write("\u00c6\7c\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\24\3\2\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7v\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write("\u00cf\7i\2\2\u00cf\26\3\2\2\2\u00d0\u00d1\7k\2\2\u00d1")
        buf.write("\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\30\3\2\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7q\2\2\u00d7")
        buf.write("\u00d8\7c\2\2\u00d8\u00d9\7v\2\2\u00d9\32\3\2\2\2\u00da")
        buf.write("\u00db\7d\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7q\2\2\u00dd")
        buf.write("\u00de\7n\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7c\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\34\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7u\2\2\u00e6")
        buf.write("\u00e7\7v\2\2\u00e7\36\3\2\2\2\u00e8\u00e9\7x\2\2\u00e9")
        buf.write("\u00ea\7c\2\2\u00ea\u00eb\7t\2\2\u00eb \3\2\2\2\u00ec")
        buf.write("\u00ed\7e\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\u00f0\7v\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2")
        buf.write("\u00f3\7w\2\2\u00f3\u00f4\7g\2\2\u00f4\"\3\2\2\2\u00f5")
        buf.write("\u00f6\7d\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7g\2\2\u00f8")
        buf.write("\u00f9\7c\2\2\u00f9\u00fa\7m\2\2\u00fa$\3\2\2\2\u00fb")
        buf.write("\u00fc\7t\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7p\2\2\u00fe")
        buf.write("\u00ff\7i\2\2\u00ff\u0100\7g\2\2\u0100&\3\2\2\2\u0101")
        buf.write("\u0102\7p\2\2\u0102\u0103\7k\2\2\u0103\u0104\7n\2\2\u0104")
        buf.write("(\3\2\2\2\u0105\u0106\7v\2\2\u0106\u0107\7t\2\2\u0107")
        buf.write("\u0108\7w\2\2\u0108\u0109\7g\2\2\u0109*\3\2\2\2\u010a")
        buf.write("\u010b\7h\2\2\u010b\u010c\7c\2\2\u010c\u010d\7n\2\2\u010d")
        buf.write("\u010e\7u\2\2\u010e\u010f\7g\2\2\u010f,\3\2\2\2\u0110")
        buf.write("\u0111\7R\2\2\u0111\u0112\7w\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\u0114\7U\2\2\u0114\u0115\7v\2\2\u0115\u0116\7t\2\2\u0116")
        buf.write("\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119\7i\2\2\u0119")
        buf.write("\u011a\7N\2\2\u011a\u011b\7p\2\2\u011b.\3\2\2\2\u011c")
        buf.write("\u011d\7R\2\2\u011d\u011e\7w\2\2\u011e\u011f\7v\2\2\u011f")
        buf.write("\u0120\7K\2\2\u0120\u0121\7p\2\2\u0121\u0122\7v\2\2\u0122")
        buf.write("\u0123\7N\2\2\u0123\u0124\7p\2\2\u0124\60\3\2\2\2\u0125")
        buf.write("\u0126\7-\2\2\u0126\62\3\2\2\2\u0127\u0128\7/\2\2\u0128")
        buf.write("\64\3\2\2\2\u0129\u012a\7,\2\2\u012a\66\3\2\2\2\u012b")
        buf.write("\u012c\7\61\2\2\u012c8\3\2\2\2\u012d\u012e\7\'\2\2\u012e")
        buf.write(":\3\2\2\2\u012f\u0130\7?\2\2\u0130\u0131\7?\2\2\u0131")
        buf.write("<\3\2\2\2\u0132\u0133\7#\2\2\u0133\u0134\7?\2\2\u0134")
        buf.write(">\3\2\2\2\u0135\u0136\7>\2\2\u0136\u0137\7?\2\2\u0137")
        buf.write("@\3\2\2\2\u0138\u0139\7@\2\2\u0139\u013a\7?\2\2\u013a")
        buf.write("B\3\2\2\2\u013b\u013c\7>\2\2\u013cD\3\2\2\2\u013d\u013e")
        buf.write("\7@\2\2\u013eF\3\2\2\2\u013f\u0140\7(\2\2\u0140\u0141")
        buf.write("\7(\2\2\u0141H\3\2\2\2\u0142\u0143\7~\2\2\u0143\u0144")
        buf.write("\7~\2\2\u0144J\3\2\2\2\u0145\u0146\7#\2\2\u0146L\3\2\2")
        buf.write("\2\u0147\u0148\7-\2\2\u0148\u0149\7?\2\2\u0149N\3\2\2")
        buf.write("\2\u014a\u014b\7/\2\2\u014b\u014c\7?\2\2\u014cP\3\2\2")
        buf.write("\2\u014d\u014e\7,\2\2\u014e\u014f\7?\2\2\u014fR\3\2\2")
        buf.write("\2\u0150\u0151\7\61\2\2\u0151\u0152\7?\2\2\u0152T\3\2")
        buf.write("\2\2\u0153\u0154\7\'\2\2\u0154\u0155\7?\2\2\u0155V\3\2")
        buf.write("\2\2\u0156\u0157\7<\2\2\u0157\u0158\7?\2\2\u0158X\3\2")
        buf.write("\2\2\u0159\u015a\7?\2\2\u015aZ\3\2\2\2\u015b\u015c\7\60")
        buf.write("\2\2\u015c\\\3\2\2\2\u015d\u015e\7*\2\2\u015e^\3\2\2\2")
        buf.write("\u015f\u0160\7+\2\2\u0160`\3\2\2\2\u0161\u0162\7}\2\2")
        buf.write("\u0162b\3\2\2\2\u0163\u0164\7\177\2\2\u0164d\3\2\2\2\u0165")
        buf.write("\u0166\7]\2\2\u0166f\3\2\2\2\u0167\u0168\7_\2\2\u0168")
        buf.write("h\3\2\2\2\u0169\u016a\7.\2\2\u016aj\3\2\2\2\u016b\u016c")
        buf.write("\7=\2\2\u016cl\3\2\2\2\u016d\u0171\t\2\2\2\u016e\u0170")
        buf.write("\t\3\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172n\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u017d\7\62\2\2\u0175\u0179\t\4\2")
        buf.write("\2\u0176\u0178\t\5\2\2\u0177\u0176\3\2\2\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u0174\3\2\2\2")
        buf.write("\u017c\u0175\3\2\2\2\u017dp\3\2\2\2\u017e\u017f\7\62\2")
        buf.write("\2\u017f\u0181\t\6\2\2\u0180\u0182\5{>\2\u0181\u0180\3")
        buf.write("\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\b9\2\2\u0186")
        buf.write("r\3\2\2\2\u0187\u0188\7\62\2\2\u0188\u018a\t\7\2\2\u0189")
        buf.write("\u018b\5y=\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u018f\b:\3\2\u018ft\3\2\2\2\u0190\u0191\7\62\2")
        buf.write("\2\u0191\u0193\t\b\2\2\u0192\u0194\5w<\2\u0193\u0192\3")
        buf.write("\2\2\2\u0194\u0195\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\b;\4\2\u0198")
        buf.write("v\3\2\2\2\u0199\u019a\t\t\2\2\u019ax\3\2\2\2\u019b\u019c")
        buf.write("\t\n\2\2\u019cz\3\2\2\2\u019d\u019e\t\13\2\2\u019e|\3")
        buf.write("\2\2\2\u019f\u01a1\t\f\2\2\u01a0\u01a2\t\r\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01ab\3\2\2\2\u01a3")
        buf.write("\u01ac\7\62\2\2\u01a4\u01a8\t\4\2\2\u01a5\u01a7\t\5\2")
        buf.write("\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01ab\u01a3\3\2\2\2\u01ab\u01a4\3\2\2\2")
        buf.write("\u01ac~\3\2\2\2\u01ad\u01ae\5\u0081A\2\u01ae\u01b2\7\60")
        buf.write("\2\2\u01af\u01b1\t\5\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b7\5}?\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01c8\3\2\2\2")
        buf.write("\u01b8\u01ba\7\60\2\2\u01b9\u01bb\t\5\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01c0\5}?\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c8\3\2\2\2")
        buf.write("\u01c1\u01c3\t\5\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6")
        buf.write("\3\2\2\2\u01c6\u01c8\5}?\2\u01c7\u01ad\3\2\2\2\u01c7\u01b8")
        buf.write("\3\2\2\2\u01c7\u01c2\3\2\2\2\u01c8\u0080\3\2\2\2\u01c9")
        buf.write("\u01d2\7\62\2\2\u01ca\u01ce\t\4\2\2\u01cb\u01cd\t\5\2")
        buf.write("\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d1\u01c9\3\2\2\2\u01d1\u01ca\3\2\2\2")
        buf.write("\u01d2\u0082\3\2\2\2\u01d3\u01db\7$\2\2\u01d4\u01da\n")
        buf.write("\16\2\2\u01d5\u01d6\7^\2\2\u01d6\u01da\t\17\2\2\u01d7")
        buf.write("\u01d8\7)\2\2\u01d8\u01da\7$\2\2\u01d9\u01d4\3\2\2\2\u01d9")
        buf.write("\u01d5\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01dd\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01de\3")
        buf.write("\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01df\7$\2\2\u01df\u01e0")
        buf.write("\bB\5\2\u01e0\u0084\3\2\2\2\u01e1\u01e2\7v\2\2\u01e2\u01e3")
        buf.write("\7t\2\2\u01e3\u01e4\7w\2\2\u01e4\u01eb\7g\2\2\u01e5\u01e6")
        buf.write("\7h\2\2\u01e6\u01e7\7c\2\2\u01e7\u01e8\7n\2\2\u01e8\u01e9")
        buf.write("\7u\2\2\u01e9\u01eb\7g\2\2\u01ea\u01e1\3\2\2\2\u01ea\u01e5")
        buf.write("\3\2\2\2\u01eb\u0086\3\2\2\2\u01ec\u01ed\7p\2\2\u01ed")
        buf.write("\u01ee\7k\2\2\u01ee\u01ef\7n\2\2\u01ef\u0088\3\2\2\2\u01f0")
        buf.write("\u01f1\7\61\2\2\u01f1\u01f2\7\61\2\2\u01f2\u01f6\3\2\2")
        buf.write("\2\u01f3\u01f5\n\20\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8")
        buf.write("\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f9\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fa\bE\6\2")
        buf.write("\u01fa\u008a\3\2\2\2\u01fb\u01fc\7\61\2\2\u01fc\u01fd")
        buf.write("\7,\2\2\u01fd\u0202\3\2\2\2\u01fe\u0201\5\u008bF\2\u01ff")
        buf.write("\u0201\13\2\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff\3\2\2")
        buf.write("\2\u0201\u0204\3\2\2\2\u0202\u0203\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3\2\2\2\u0205")
        buf.write("\u0206\7,\2\2\u0206\u0207\7\61\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u0209\bF\6\2\u0209\u008c\3\2\2\2\u020a\u020c\t")
        buf.write("\21\2\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020f\u0210\bG\6\2\u0210\u008e\3\2\2\2\u0211\u0212\13")
        buf.write("\2\2\2\u0212\u0213\bH\7\2\u0213\u0090\3\2\2\2\u0214\u021c")
        buf.write("\7$\2\2\u0215\u021b\n\16\2\2\u0216\u0217\7^\2\2\u0217")
        buf.write("\u021b\t\17\2\2\u0218\u0219\7)\2\2\u0219\u021b\7$\2\2")
        buf.write("\u021a\u0215\3\2\2\2\u021a\u0216\3\2\2\2\u021a\u0218\3")
        buf.write("\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d")
        buf.write("\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021f")
        buf.write("\u0221\t\22\2\2\u0220\u021f\3\2\2\2\u0221\u0222\3\2\2")
        buf.write("\2\u0222\u0223\bI\b\2\u0223\u0092\3\2\2\2\u0224\u0225")
        buf.write("\t\17\2\2\u0225\u0094\3\2\2\2\u0226\u022e\7$\2\2\u0227")
        buf.write("\u022d\n\16\2\2\u0228\u0229\7^\2\2\u0229\u022d\t\17\2")
        buf.write("\2\u022a\u022b\7)\2\2\u022b\u022d\7$\2\2\u022c\u0227\3")
        buf.write("\2\2\2\u022c\u0228\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u0230")
        buf.write("\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f")
        buf.write("\u0231\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232\7^\2\2")
        buf.write("\u0232\u0233\n\23\2\2\u0233\u0234\bK\t\2\u0234\u0096\3")
        buf.write("\2\2\2\u0235\u0236\7c\2\2\u0236\u0237\7t\2\2\u0237\u0238")
        buf.write("\7t\2\2\u0238\u0239\7c\2\2\u0239\u023a\7{\2\2\u023a\u0098")
        buf.write("\3\2\2\2 \2\u0171\u0179\u017c\u0183\u018c\u0195\u01a1")
        buf.write("\u01a8\u01ab\u01b2\u01b6\u01bc\u01bf\u01c4\u01c7\u01ce")
        buf.write("\u01d1\u01d9\u01db\u01ea\u01f6\u0200\u0202\u020d\u021a")
        buf.write("\u021c\u0220\u022c\u022e\n\39\2\3:\3\3;\4\3B\5\b\2\2\3")
        buf.write("H\6\3I\7\3K\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    PUTSTRINGLN = 22
    PUTINTLN = 23
    PLUS = 24
    MINUS = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQUAL = 29
    NOTEQUAL = 30
    LE = 31
    GE = 32
    LT = 33
    GT = 34
    AND = 35
    OR = 36
    NOT = 37
    PLUSEQ = 38
    MINUSEQ = 39
    MULEQ = 40
    DIVEQ = 41
    MODEQ = 42
    COLONEQ = 43
    ASSIGN = 44
    DOT = 45
    LPAREN = 46
    RPAREN = 47
    LBRACE = 48
    RBRACE = 49
    LBRACK = 50
    RBRACK = 51
    COMMA = 52
    SEMI = 53
    ID = 54
    DECIMAL_LIT = 55
    BINARY_LIT = 56
    OCT_LIT = 57
    HEXA_LIT = 58
    FLOAT_LIT = 59
    STRING_LIT = 60
    BOOLEAN_LIT = 61
    NIL_LIT = 62
    SINGLE_LINE_COMMENT = 63
    MULTI_LINE_COMMENT = 64
    WS = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    VALID_ESCAPES = 68
    ILLEGAL_ESCAPE = 69
    ARRAY = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'true'", 
            "'false'", "'PutStringLn'", "'PutIntLn'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", 
            "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "':='", "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "','", "';'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PUTSTRINGLN", "PUTINTLN", 
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LE", 
            "GE", "LT", "GT", "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", 
            "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", "ID", 
            "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", "HEXA_LIT", "FLOAT_LIT", 
            "STRING_LIT", "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", 
            "MULTI_LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "VALID_ESCAPES", "ILLEGAL_ESCAPE", "ARRAY" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "PUTSTRINGLN", "PUTINTLN", "PLUS", "MINUS", "MUL", 
                  "DIV", "MOD", "EQUAL", "NOTEQUAL", "LE", "GE", "LT", "GT", 
                  "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", "DIVEQ", 
                  "MODEQ", "COLONEQ", "ASSIGN", "DOT", "LPAREN", "RPAREN", 
                  "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", 
                  "ID", "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", "HEXA_LIT", 
                  "HEX_DIGIT", "OCTAL_DIGIT", "BIN_DIGIT", "EXP", "FLOAT_LIT", 
                  "DECIMALS", "STRING_LIT", "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "VALID_ESCAPES", "ILLEGAL_ESCAPE", "ARRAY" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.BINARY_LIT_action 
            actions[56] = self.OCT_LIT_action 
            actions[57] = self.HEXA_LIT_action 
            actions[64] = self.STRING_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def BINARY_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = str(int(self.text, 2)) 
     

    def OCT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = str(int(self.text, 8)) 
     

    def HEXA_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = str(int(self.text, 16)) 
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2]) 
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1]) 
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                VAL_ESCAPES = ['n', 't', 'r', '"', '\\']
                for i in range(1, len(self.text)-1):
                    if self.text[i] == '\\' and self.text[i+1] not in VAL_ESCAPES:
                        raise IllegalEscape(self.text[1:i+2])

     


