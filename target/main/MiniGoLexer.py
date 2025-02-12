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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u0245\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3")
        buf.write("/\3/\3/\5/\u0166\n/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\7")
        buf.write("8\u017a\n8\f8\168\u017d\138\39\39\39\79\u0182\n9\f9\16")
        buf.write("9\u0185\139\59\u0187\n9\3:\3:\3:\6:\u018c\n:\r:\16:\u018d")
        buf.write("\3:\3:\3;\3;\3;\6;\u0195\n;\r;\16;\u0196\3;\3;\3<\3<\3")
        buf.write("<\6<\u019e\n<\r<\16<\u019f\3<\3<\3=\3=\3>\3>\3?\3?\3@")
        buf.write("\3@\5@\u01ac\n@\3@\3@\3@\7@\u01b1\n@\f@\16@\u01b4\13@")
        buf.write("\5@\u01b6\n@\3A\3A\3A\7A\u01bb\nA\fA\16A\u01be\13A\3A")
        buf.write("\5A\u01c1\nA\3A\3A\6A\u01c5\nA\rA\16A\u01c6\3A\5A\u01ca")
        buf.write("\nA\3A\6A\u01cd\nA\rA\16A\u01ce\3A\5A\u01d2\nA\3B\3B\3")
        buf.write("B\7B\u01d7\nB\fB\16B\u01da\13B\5B\u01dc\nB\3C\3C\3C\3")
        buf.write("C\3C\3C\7C\u01e4\nC\fC\16C\u01e7\13C\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\5D\u01f5\nD\3E\3E\3E\3E\3F\3F\3F\3")
        buf.write("F\7F\u01ff\nF\fF\16F\u0202\13F\3F\3F\3G\3G\3G\3G\3G\7")
        buf.write("G\u020b\nG\fG\16G\u020e\13G\3G\3G\3G\3G\3G\3H\6H\u0216")
        buf.write("\nH\rH\16H\u0217\3H\3H\3I\3I\3I\3J\3J\3J\3J\3J\3J\7J\u0225")
        buf.write("\nJ\fJ\16J\u0228\13J\3J\5J\u022b\nJ\3J\3J\3K\3K\3L\3L")
        buf.write("\3L\3L\3L\3L\7L\u0237\nL\fL\16L\u023a\13L\3L\3L\3L\3L")
        buf.write("\3M\3M\3M\3M\3M\3M\3\u020c\2N\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177\2\u0081")
        buf.write(">\u0083\2\u0085?\u0087@\u0089A\u008bB\u008dC\u008fD\u0091")
        buf.write("E\u0093F\u0095G\u0097H\u0099I\3\2\24\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2DDdd\4\2QQqq\4\2ZZzz\5\2\62")
        buf.write(";CHch\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2\f\f$$^^\7")
        buf.write("\2$$^^ppttvv\4\2\f\f\17\17\5\2\13\f\16\17\"\"\3\3\f\f")
        buf.write("\7\2))^^ppttvv\2\u0264\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2")
        buf.write("\2\5\u009d\3\2\2\2\7\u00a0\3\2\2\2\t\u00a5\3\2\2\2\13")
        buf.write("\u00a9\3\2\2\2\r\u00b0\3\2\2\2\17\u00b5\3\2\2\2\21\u00ba")
        buf.write("\3\2\2\2\23\u00c1\3\2\2\2\25\u00cb\3\2\2\2\27\u00d2\3")
        buf.write("\2\2\2\31\u00d6\3\2\2\2\33\u00dc\3\2\2\2\35\u00e4\3\2")
        buf.write("\2\2\37\u00ea\3\2\2\2!\u00ee\3\2\2\2#\u00f7\3\2\2\2%\u00fd")
        buf.write("\3\2\2\2\'\u0103\3\2\2\2)\u0107\3\2\2\2+\u010c\3\2\2\2")
        buf.write("-\u0112\3\2\2\2/\u011e\3\2\2\2\61\u0127\3\2\2\2\63\u0129")
        buf.write("\3\2\2\2\65\u012b\3\2\2\2\67\u012d\3\2\2\29\u012f\3\2")
        buf.write("\2\2;\u0131\3\2\2\2=\u0134\3\2\2\2?\u0137\3\2\2\2A\u013a")
        buf.write("\3\2\2\2C\u013d\3\2\2\2E\u013f\3\2\2\2G\u0141\3\2\2\2")
        buf.write("I\u0144\3\2\2\2K\u0147\3\2\2\2M\u0149\3\2\2\2O\u014c\3")
        buf.write("\2\2\2Q\u014f\3\2\2\2S\u0152\3\2\2\2U\u0155\3\2\2\2W\u0158")
        buf.write("\3\2\2\2Y\u015b\3\2\2\2[\u015d\3\2\2\2]\u0165\3\2\2\2")
        buf.write("_\u0167\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2e\u016d\3")
        buf.write("\2\2\2g\u016f\3\2\2\2i\u0171\3\2\2\2k\u0173\3\2\2\2m\u0175")
        buf.write("\3\2\2\2o\u0177\3\2\2\2q\u0186\3\2\2\2s\u0188\3\2\2\2")
        buf.write("u\u0191\3\2\2\2w\u019a\3\2\2\2y\u01a3\3\2\2\2{\u01a5\3")
        buf.write("\2\2\2}\u01a7\3\2\2\2\177\u01a9\3\2\2\2\u0081\u01d1\3")
        buf.write("\2\2\2\u0083\u01db\3\2\2\2\u0085\u01dd\3\2\2\2\u0087\u01f4")
        buf.write("\3\2\2\2\u0089\u01f6\3\2\2\2\u008b\u01fa\3\2\2\2\u008d")
        buf.write("\u0205\3\2\2\2\u008f\u0215\3\2\2\2\u0091\u021b\3\2\2\2")
        buf.write("\u0093\u021e\3\2\2\2\u0095\u022e\3\2\2\2\u0097\u0230\3")
        buf.write("\2\2\2\u0099\u023f\3\2\2\2\u009b\u009c\7<\2\2\u009c\4")
        buf.write("\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f\6")
        buf.write("\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\b\3\2\2\2\u00a5\u00a6")
        buf.write("\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\n")
        buf.write("\3\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\f\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7e\2\2\u00b4\16")
        buf.write("\3\2\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7{\2\2\u00b7\u00b8")
        buf.write("\7r\2\2\u00b8\u00b9\7g\2\2\u00b9\20\3\2\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7w\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0\22")
        buf.write("\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\24\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\26\3\2\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\30")
        buf.write("\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db\32")
        buf.write("\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7p\2\2\u00e3\34\3\2\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7v\2\2\u00e9\36\3\2\2\2\u00ea\u00eb")
        buf.write("\7x\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00ed \3")
        buf.write("\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6\"")
        buf.write("\3\2\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fc$\3")
        buf.write("\2\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7i\2\2\u0101\u0102\7g\2\2\u0102&\3")
        buf.write("\2\2\2\u0103\u0104\7p\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106(\3\2\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g\2\2\u010b*\3")
        buf.write("\2\2\2\u010c\u010d\7h\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7u\2\2\u0110\u0111\7g\2\2\u0111,\3")
        buf.write("\2\2\2\u0112\u0113\7R\2\2\u0113\u0114\7w\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\u0116\7U\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b")
        buf.write("\7i\2\2\u011b\u011c\7N\2\2\u011c\u011d\7p\2\2\u011d.\3")
        buf.write("\2\2\2\u011e\u011f\7R\2\2\u011f\u0120\7w\2\2\u0120\u0121")
        buf.write("\7v\2\2\u0121\u0122\7K\2\2\u0122\u0123\7p\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7N\2\2\u0125\u0126\7p\2\2\u0126\60")
        buf.write("\3\2\2\2\u0127\u0128\7-\2\2\u0128\62\3\2\2\2\u0129\u012a")
        buf.write("\7/\2\2\u012a\64\3\2\2\2\u012b\u012c\7,\2\2\u012c\66\3")
        buf.write("\2\2\2\u012d\u012e\7\61\2\2\u012e8\3\2\2\2\u012f\u0130")
        buf.write("\7\'\2\2\u0130:\3\2\2\2\u0131\u0132\7?\2\2\u0132\u0133")
        buf.write("\7?\2\2\u0133<\3\2\2\2\u0134\u0135\7#\2\2\u0135\u0136")
        buf.write("\7?\2\2\u0136>\3\2\2\2\u0137\u0138\7>\2\2\u0138\u0139")
        buf.write("\7?\2\2\u0139@\3\2\2\2\u013a\u013b\7@\2\2\u013b\u013c")
        buf.write("\7?\2\2\u013cB\3\2\2\2\u013d\u013e\7>\2\2\u013eD\3\2\2")
        buf.write("\2\u013f\u0140\7@\2\2\u0140F\3\2\2\2\u0141\u0142\7(\2")
        buf.write("\2\u0142\u0143\7(\2\2\u0143H\3\2\2\2\u0144\u0145\7~\2")
        buf.write("\2\u0145\u0146\7~\2\2\u0146J\3\2\2\2\u0147\u0148\7#\2")
        buf.write("\2\u0148L\3\2\2\2\u0149\u014a\7-\2\2\u014a\u014b\7?\2")
        buf.write("\2\u014bN\3\2\2\2\u014c\u014d\7/\2\2\u014d\u014e\7?\2")
        buf.write("\2\u014eP\3\2\2\2\u014f\u0150\7,\2\2\u0150\u0151\7?\2")
        buf.write("\2\u0151R\3\2\2\2\u0152\u0153\7\61\2\2\u0153\u0154\7?")
        buf.write("\2\2\u0154T\3\2\2\2\u0155\u0156\7\'\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157V\3\2\2\2\u0158\u0159\7<\2\2\u0159\u015a\7")
        buf.write("?\2\2\u015aX\3\2\2\2\u015b\u015c\7?\2\2\u015cZ\3\2\2\2")
        buf.write("\u015d\u015e\7\60\2\2\u015e\\\3\2\2\2\u015f\u0166\5W,")
        buf.write("\2\u0160\u0166\5M\'\2\u0161\u0166\5O(\2\u0162\u0166\5")
        buf.write("Q)\2\u0163\u0166\5S*\2\u0164\u0166\5U+\2\u0165\u015f\3")
        buf.write("\2\2\2\u0165\u0160\3\2\2\2\u0165\u0161\3\2\2\2\u0165\u0162")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("^\3\2\2\2\u0167\u0168\7*\2\2\u0168`\3\2\2\2\u0169\u016a")
        buf.write("\7+\2\2\u016ab\3\2\2\2\u016b\u016c\7}\2\2\u016cd\3\2\2")
        buf.write("\2\u016d\u016e\7\177\2\2\u016ef\3\2\2\2\u016f\u0170\7")
        buf.write("]\2\2\u0170h\3\2\2\2\u0171\u0172\7_\2\2\u0172j\3\2\2\2")
        buf.write("\u0173\u0174\7.\2\2\u0174l\3\2\2\2\u0175\u0176\7=\2\2")
        buf.write("\u0176n\3\2\2\2\u0177\u017b\t\2\2\2\u0178\u017a\t\3\2")
        buf.write("\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017cp\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u0187\7\62\2\2\u017f\u0183\t\4\2\2\u0180")
        buf.write("\u0182\t\5\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0187\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0186\u017e\3\2\2\2\u0186\u017f")
        buf.write("\3\2\2\2\u0187r\3\2\2\2\u0188\u0189\7\62\2\2\u0189\u018b")
        buf.write("\t\6\2\2\u018a\u018c\5}?\2\u018b\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0190\b:\2\2\u0190t\3\2\2\2\u0191")
        buf.write("\u0192\7\62\2\2\u0192\u0194\t\7\2\2\u0193\u0195\5{>\2")
        buf.write("\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199")
        buf.write("\b;\3\2\u0199v\3\2\2\2\u019a\u019b\7\62\2\2\u019b\u019d")
        buf.write("\t\b\2\2\u019c\u019e\5y=\2\u019d\u019c\3\2\2\2\u019e\u019f")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a2\b<\4\2\u01a2x\3\2\2\2\u01a3")
        buf.write("\u01a4\t\t\2\2\u01a4z\3\2\2\2\u01a5\u01a6\t\n\2\2\u01a6")
        buf.write("|\3\2\2\2\u01a7\u01a8\t\13\2\2\u01a8~\3\2\2\2\u01a9\u01ab")
        buf.write("\t\f\2\2\u01aa\u01ac\t\r\2\2\u01ab\u01aa\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01b5\3\2\2\2\u01ad\u01b6\7\62\2")
        buf.write("\2\u01ae\u01b2\t\4\2\2\u01af\u01b1\t\5\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01ad\3\2\2\2\u01b5\u01ae\3\2\2\2\u01b6\u0080\3")
        buf.write("\2\2\2\u01b7\u01b8\5\u0083B\2\u01b8\u01bc\7\60\2\2\u01b9")
        buf.write("\u01bb\t\5\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2")
        buf.write("\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01c0\3")
        buf.write("\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\5\177@\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01d2\3\2\2\2")
        buf.write("\u01c2\u01c4\7\60\2\2\u01c3\u01c5\t\5\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01ca\5\177@")
        buf.write("\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01d2")
        buf.write("\3\2\2\2\u01cb\u01cd\t\5\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d0\3\2\2\2\u01d0\u01d2\5\177@\2\u01d1\u01b7")
        buf.write("\3\2\2\2\u01d1\u01c2\3\2\2\2\u01d1\u01cc\3\2\2\2\u01d2")
        buf.write("\u0082\3\2\2\2\u01d3\u01dc\7\62\2\2\u01d4\u01d8\t\4\2")
        buf.write("\2\u01d5\u01d7\t\5\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01d3\3\2\2\2")
        buf.write("\u01db\u01d4\3\2\2\2\u01dc\u0084\3\2\2\2\u01dd\u01e5\7")
        buf.write("$\2\2\u01de\u01e4\n\16\2\2\u01df\u01e0\7^\2\2\u01e0\u01e4")
        buf.write("\t\17\2\2\u01e1\u01e2\7)\2\2\u01e2\u01e4\7$\2\2\u01e3")
        buf.write("\u01de\3\2\2\2\u01e3\u01df\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9")
        buf.write("\7$\2\2\u01e9\u01ea\bC\5\2\u01ea\u0086\3\2\2\2\u01eb\u01ec")
        buf.write("\7v\2\2\u01ec\u01ed\7t\2\2\u01ed\u01ee\7w\2\2\u01ee\u01f5")
        buf.write("\7g\2\2\u01ef\u01f0\7h\2\2\u01f0\u01f1\7c\2\2\u01f1\u01f2")
        buf.write("\7n\2\2\u01f2\u01f3\7u\2\2\u01f3\u01f5\7g\2\2\u01f4\u01eb")
        buf.write("\3\2\2\2\u01f4\u01ef\3\2\2\2\u01f5\u0088\3\2\2\2\u01f6")
        buf.write("\u01f7\7p\2\2\u01f7\u01f8\7k\2\2\u01f8\u01f9\7n\2\2\u01f9")
        buf.write("\u008a\3\2\2\2\u01fa\u01fb\7\61\2\2\u01fb\u01fc\7\61\2")
        buf.write("\2\u01fc\u0200\3\2\2\2\u01fd\u01ff\n\20\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0203\u0204\bF\6\2\u0204\u008c\3\2\2\2\u0205\u0206\7")
        buf.write("\61\2\2\u0206\u0207\7,\2\2\u0207\u020c\3\2\2\2\u0208\u020b")
        buf.write("\5\u008dG\2\u0209\u020b\13\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020f\u0210\7,\2\2\u0210\u0211\7\61\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212\u0213\bG\6\2\u0213\u008e\3\2\2\2\u0214")
        buf.write("\u0216\t\21\2\2\u0215\u0214\3\2\2\2\u0216\u0217\3\2\2")
        buf.write("\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021a\bH\6\2\u021a\u0090\3\2\2\2\u021b")
        buf.write("\u021c\13\2\2\2\u021c\u021d\bI\7\2\u021d\u0092\3\2\2\2")
        buf.write("\u021e\u0226\7$\2\2\u021f\u0225\n\16\2\2\u0220\u0221\7")
        buf.write("^\2\2\u0221\u0225\t\17\2\2\u0222\u0223\7)\2\2\u0223\u0225")
        buf.write("\7$\2\2\u0224\u021f\3\2\2\2\u0224\u0220\3\2\2\2\u0224")
        buf.write("\u0222\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3")
        buf.write("\2\2\2\u0229\u022b\t\22\2\2\u022a\u0229\3\2\2\2\u022b")
        buf.write("\u022c\3\2\2\2\u022c\u022d\bJ\b\2\u022d\u0094\3\2\2\2")
        buf.write("\u022e\u022f\t\17\2\2\u022f\u0096\3\2\2\2\u0230\u0238")
        buf.write("\7$\2\2\u0231\u0237\n\16\2\2\u0232\u0233\7^\2\2\u0233")
        buf.write("\u0237\t\17\2\2\u0234\u0235\7)\2\2\u0235\u0237\7$\2\2")
        buf.write("\u0236\u0231\3\2\2\2\u0236\u0232\3\2\2\2\u0236\u0234\3")
        buf.write("\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239")
        buf.write("\3\2\2\2\u0239\u023b\3\2\2\2\u023a\u0238\3\2\2\2\u023b")
        buf.write("\u023c\7^\2\2\u023c\u023d\n\23\2\2\u023d\u023e\bL\t\2")
        buf.write("\u023e\u0098\3\2\2\2\u023f\u0240\7c\2\2\u0240\u0241\7")
        buf.write("t\2\2\u0241\u0242\7t\2\2\u0242\u0243\7c\2\2\u0243\u0244")
        buf.write("\7{\2\2\u0244\u009a\3\2\2\2!\2\u0165\u017b\u0183\u0186")
        buf.write("\u018d\u0196\u019f\u01ab\u01b2\u01b5\u01bc\u01c0\u01c6")
        buf.write("\u01c9\u01ce\u01d1\u01d8\u01db\u01e3\u01e5\u01f4\u0200")
        buf.write("\u020a\u020c\u0217\u0224\u0226\u022a\u0236\u0238\n\3:")
        buf.write("\2\3;\3\3<\4\3C\5\b\2\2\3I\6\3J\7\3L\b")
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
    ASSIGN_OPERATOR = 46
    LPAREN = 47
    RPAREN = 48
    LBRACE = 49
    RBRACE = 50
    LBRACK = 51
    RBRACK = 52
    COMMA = 53
    SEMI = 54
    ID = 55
    DECIMAL_LIT = 56
    BINARY_LIT = 57
    OCT_LIT = 58
    HEXA_LIT = 59
    FLOAT_LIT = 60
    STRING_LIT = 61
    BOOLEAN_LIT = 62
    NIL_LIT = 63
    SINGLE_LINE_COMMENT = 64
    MULTI_LINE_COMMENT = 65
    WS = 66
    ERROR_CHAR = 67
    UNCLOSE_STRING = 68
    VALID_ESCAPES = 69
    ILLEGAL_ESCAPE = 70
    ARRAY = 71

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
            "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", "ASSIGN_OPERATOR", 
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", 
            "HEXA_LIT", "FLOAT_LIT", "STRING_LIT", "BOOLEAN_LIT", "NIL_LIT", 
            "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "VALID_ESCAPES", "ILLEGAL_ESCAPE", "ARRAY" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "PUTSTRINGLN", "PUTINTLN", "PLUS", "MINUS", "MUL", 
                  "DIV", "MOD", "EQUAL", "NOTEQUAL", "LE", "GE", "LT", "GT", 
                  "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", "DIVEQ", 
                  "MODEQ", "COLONEQ", "ASSIGN", "DOT", "ASSIGN_OPERATOR", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", 
                  "HEXA_LIT", "HEX_DIGIT", "OCTAL_DIGIT", "BIN_DIGIT", "EXP", 
                  "FLOAT_LIT", "DECIMALS", "STRING_LIT", "BOOLEAN_LIT", 
                  "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "VALID_ESCAPES", 
                  "ILLEGAL_ESCAPE", "ARRAY" ]

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
            actions[56] = self.BINARY_LIT_action 
            actions[57] = self.OCT_LIT_action 
            actions[58] = self.HEXA_LIT_action 
            actions[65] = self.STRING_LIT_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
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

     


