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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u021a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\7\65\u0155\n\65\f\65\16\65\u0158\13\65\3\66\3")
        buf.write("\66\3\66\7\66\u015d\n\66\f\66\16\66\u0160\13\66\5\66\u0162")
        buf.write("\n\66\3\67\3\67\3\67\6\67\u0167\n\67\r\67\16\67\u0168")
        buf.write("\3\67\3\67\38\38\38\68\u0170\n8\r8\168\u0171\38\38\39")
        buf.write("\39\39\69\u0179\n9\r9\169\u017a\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\5=\u0187\n=\3=\3=\3=\7=\u018c\n=\f=\16=\u018f")
        buf.write("\13=\5=\u0191\n=\3>\3>\3>\7>\u0196\n>\f>\16>\u0199\13")
        buf.write(">\3>\5>\u019c\n>\3>\3>\6>\u01a0\n>\r>\16>\u01a1\3>\5>")
        buf.write("\u01a5\n>\3>\6>\u01a8\n>\r>\16>\u01a9\3>\5>\u01ad\n>\3")
        buf.write("?\3?\3?\7?\u01b2\n?\f?\16?\u01b5\13?\5?\u01b7\n?\3@\3")
        buf.write("@\3@\3@\3@\3@\7@\u01bf\n@\f@\16@\u01c2\13@\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u01d0\nA\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3C\7C\u01da\nC\fC\16C\u01dd\13C\3C\3C\3D\3D\3D\3")
        buf.write("D\3D\7D\u01e6\nD\fD\16D\u01e9\13D\3D\3D\3D\3D\3D\3E\6")
        buf.write("E\u01f1\nE\rE\16E\u01f2\3E\3E\3F\3F\3F\3G\3G\3G\3G\3G")
        buf.write("\3G\7G\u0200\nG\fG\16G\u0203\13G\3G\5G\u0206\nG\3G\3G")
        buf.write("\3H\3H\3I\3I\3I\3I\3I\3I\7I\u0212\nI\fI\16I\u0215\13I")
        buf.write("\3I\3I\3I\3I\3\u01e7\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s\2u\2w\2y\2{;}\2\177<\u0081=\u0083")
        buf.write(">\u0085?\u0087@\u0089A\u008bB\u008dC\u008fD\u0091E\3\2")
        buf.write("\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd")
        buf.write("\4\2QQqq\4\2ZZzz\5\2\62;CHch\3\2\629\3\2\62\63\4\2GGg")
        buf.write("g\4\2--//\5\2\f\f$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2")
        buf.write("\13\f\16\17\"\"\3\3\f\f\7\2))^^ppttvv\2\u0234\2\3\3\2")
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
        buf.write("\2{\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u0093\3\2\2\2\5\u0095\3\2\2\2\7\u0098\3\2\2")
        buf.write("\2\t\u009d\3\2\2\2\13\u00a1\3\2\2\2\r\u00a8\3\2\2\2\17")
        buf.write("\u00ad\3\2\2\2\21\u00b2\3\2\2\2\23\u00b9\3\2\2\2\25\u00c3")
        buf.write("\3\2\2\2\27\u00ca\3\2\2\2\31\u00ce\3\2\2\2\33\u00d4\3")
        buf.write("\2\2\2\35\u00dc\3\2\2\2\37\u00e2\3\2\2\2!\u00e6\3\2\2")
        buf.write("\2#\u00ef\3\2\2\2%\u00f5\3\2\2\2\'\u00fb\3\2\2\2)\u00ff")
        buf.write("\3\2\2\2+\u0104\3\2\2\2-\u010a\3\2\2\2/\u010c\3\2\2\2")
        buf.write("\61\u010e\3\2\2\2\63\u0110\3\2\2\2\65\u0112\3\2\2\2\67")
        buf.write("\u0114\3\2\2\29\u0117\3\2\2\2;\u011a\3\2\2\2=\u011d\3")
        buf.write("\2\2\2?\u0120\3\2\2\2A\u0122\3\2\2\2C\u0124\3\2\2\2E\u0127")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012c\3\2\2\2K\u012f\3\2\2\2")
        buf.write("M\u0132\3\2\2\2O\u0135\3\2\2\2Q\u0138\3\2\2\2S\u013b\3")
        buf.write("\2\2\2U\u013e\3\2\2\2W\u0140\3\2\2\2Y\u0142\3\2\2\2[\u0144")
        buf.write("\3\2\2\2]\u0146\3\2\2\2_\u0148\3\2\2\2a\u014a\3\2\2\2")
        buf.write("c\u014c\3\2\2\2e\u014e\3\2\2\2g\u0150\3\2\2\2i\u0152\3")
        buf.write("\2\2\2k\u0161\3\2\2\2m\u0163\3\2\2\2o\u016c\3\2\2\2q\u0175")
        buf.write("\3\2\2\2s\u017e\3\2\2\2u\u0180\3\2\2\2w\u0182\3\2\2\2")
        buf.write("y\u0184\3\2\2\2{\u01ac\3\2\2\2}\u01b6\3\2\2\2\177\u01b8")
        buf.write("\3\2\2\2\u0081\u01cf\3\2\2\2\u0083\u01d1\3\2\2\2\u0085")
        buf.write("\u01d5\3\2\2\2\u0087\u01e0\3\2\2\2\u0089\u01f0\3\2\2\2")
        buf.write("\u008b\u01f6\3\2\2\2\u008d\u01f9\3\2\2\2\u008f\u0209\3")
        buf.write("\2\2\2\u0091\u020b\3\2\2\2\u0093\u0094\7<\2\2\u0094\4")
        buf.write("\3\2\2\2\u0095\u0096\7k\2\2\u0096\u0097\7h\2\2\u0097\6")
        buf.write("\3\2\2\2\u0098\u0099\7g\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\u009c\7g\2\2\u009c\b\3\2\2\2\u009d\u009e")
        buf.write("\7h\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7t\2\2\u00a0\n")
        buf.write("\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\16")
        buf.write("\3\2\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7{\2\2\u00af\u00b0")
        buf.write("\7r\2\2\u00b0\u00b1\7g\2\2\u00b1\20\3\2\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7w\2\2\u00b6\u00b7\7e\2\2\u00b7\u00b8\7v\2\2\u00b8\22")
        buf.write("\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7i\2\2\u00c9\26\3\2\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\30")
        buf.write("\3\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\32")
        buf.write("\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7p\2\2\u00db\34\3\2\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7u\2\2\u00e0\u00e1\7v\2\2\u00e1\36\3\2\2\2\u00e2\u00e3")
        buf.write("\7x\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7t\2\2\u00e5 \3")
        buf.write("\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7g\2\2\u00ee\"")
        buf.write("\3\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7m\2\2\u00f4$\3")
        buf.write("\2\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7i\2\2\u00f9\u00fa\7g\2\2\u00fa&\3")
        buf.write("\2\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe(\3\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7w\2\2\u0102\u0103\7g\2\2\u0103*\3")
        buf.write("\2\2\2\u0104\u0105\7h\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109,\3")
        buf.write("\2\2\2\u010a\u010b\7-\2\2\u010b.\3\2\2\2\u010c\u010d\7")
        buf.write("/\2\2\u010d\60\3\2\2\2\u010e\u010f\7,\2\2\u010f\62\3\2")
        buf.write("\2\2\u0110\u0111\7\61\2\2\u0111\64\3\2\2\2\u0112\u0113")
        buf.write("\7\'\2\2\u0113\66\3\2\2\2\u0114\u0115\7?\2\2\u0115\u0116")
        buf.write("\7?\2\2\u01168\3\2\2\2\u0117\u0118\7#\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119:\3\2\2\2\u011a\u011b\7>\2\2\u011b\u011c")
        buf.write("\7?\2\2\u011c<\3\2\2\2\u011d\u011e\7@\2\2\u011e\u011f")
        buf.write("\7?\2\2\u011f>\3\2\2\2\u0120\u0121\7>\2\2\u0121@\3\2\2")
        buf.write("\2\u0122\u0123\7@\2\2\u0123B\3\2\2\2\u0124\u0125\7(\2")
        buf.write("\2\u0125\u0126\7(\2\2\u0126D\3\2\2\2\u0127\u0128\7~\2")
        buf.write("\2\u0128\u0129\7~\2\2\u0129F\3\2\2\2\u012a\u012b\7#\2")
        buf.write("\2\u012bH\3\2\2\2\u012c\u012d\7-\2\2\u012d\u012e\7?\2")
        buf.write("\2\u012eJ\3\2\2\2\u012f\u0130\7/\2\2\u0130\u0131\7?\2")
        buf.write("\2\u0131L\3\2\2\2\u0132\u0133\7,\2\2\u0133\u0134\7?\2")
        buf.write("\2\u0134N\3\2\2\2\u0135\u0136\7\61\2\2\u0136\u0137\7?")
        buf.write("\2\2\u0137P\3\2\2\2\u0138\u0139\7\'\2\2\u0139\u013a\7")
        buf.write("?\2\2\u013aR\3\2\2\2\u013b\u013c\7<\2\2\u013c\u013d\7")
        buf.write("?\2\2\u013dT\3\2\2\2\u013e\u013f\7?\2\2\u013fV\3\2\2\2")
        buf.write("\u0140\u0141\7\60\2\2\u0141X\3\2\2\2\u0142\u0143\7*\2")
        buf.write("\2\u0143Z\3\2\2\2\u0144\u0145\7+\2\2\u0145\\\3\2\2\2\u0146")
        buf.write("\u0147\7}\2\2\u0147^\3\2\2\2\u0148\u0149\7\177\2\2\u0149")
        buf.write("`\3\2\2\2\u014a\u014b\7]\2\2\u014bb\3\2\2\2\u014c\u014d")
        buf.write("\7_\2\2\u014dd\3\2\2\2\u014e\u014f\7.\2\2\u014ff\3\2\2")
        buf.write("\2\u0150\u0151\7=\2\2\u0151h\3\2\2\2\u0152\u0156\t\2\2")
        buf.write("\2\u0153\u0155\t\3\2\2\u0154\u0153\3\2\2\2\u0155\u0158")
        buf.write("\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("j\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u0162\7\62\2\2\u015a")
        buf.write("\u015e\t\4\2\2\u015b\u015d\t\5\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0159")
        buf.write("\3\2\2\2\u0161\u015a\3\2\2\2\u0162l\3\2\2\2\u0163\u0164")
        buf.write("\7\62\2\2\u0164\u0166\t\6\2\2\u0165\u0167\5w<\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\b")
        buf.write("\67\2\2\u016bn\3\2\2\2\u016c\u016d\7\62\2\2\u016d\u016f")
        buf.write("\t\7\2\2\u016e\u0170\5u;\2\u016f\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0174\b8\3\2\u0174p\3\2\2\2\u0175")
        buf.write("\u0176\7\62\2\2\u0176\u0178\t\b\2\2\u0177\u0179\5s:\2")
        buf.write("\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d")
        buf.write("\b9\4\2\u017dr\3\2\2\2\u017e\u017f\t\t\2\2\u017ft\3\2")
        buf.write("\2\2\u0180\u0181\t\n\2\2\u0181v\3\2\2\2\u0182\u0183\t")
        buf.write("\13\2\2\u0183x\3\2\2\2\u0184\u0186\t\f\2\2\u0185\u0187")
        buf.write("\t\r\2\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0190\3\2\2\2\u0188\u0191\7\62\2\2\u0189\u018d\t\4\2")
        buf.write("\2\u018a\u018c\t\5\2\2\u018b\u018a\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0188\3\2\2\2")
        buf.write("\u0190\u0189\3\2\2\2\u0191z\3\2\2\2\u0192\u0193\5}?\2")
        buf.write("\u0193\u0197\7\60\2\2\u0194\u0196\t\5\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u019a\u019c\5y=\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2")
        buf.write("\2\2\u019c\u01ad\3\2\2\2\u019d\u019f\7\60\2\2\u019e\u01a0")
        buf.write("\t\5\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a5\5y=\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2")
        buf.write("\2\2\u01a5\u01ad\3\2\2\2\u01a6\u01a8\t\5\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\5y=\2\u01ac")
        buf.write("\u0192\3\2\2\2\u01ac\u019d\3\2\2\2\u01ac\u01a7\3\2\2\2")
        buf.write("\u01ad|\3\2\2\2\u01ae\u01b7\7\62\2\2\u01af\u01b3\t\4\2")
        buf.write("\2\u01b0\u01b2\t\5\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01ae\3\2\2\2")
        buf.write("\u01b6\u01af\3\2\2\2\u01b7~\3\2\2\2\u01b8\u01c0\7$\2\2")
        buf.write("\u01b9\u01bf\n\16\2\2\u01ba\u01bb\7^\2\2\u01bb\u01bf\t")
        buf.write("\17\2\2\u01bc\u01bd\7)\2\2\u01bd\u01bf\7$\2\2\u01be\u01b9")
        buf.write("\3\2\2\2\u01be\u01ba\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7")
        buf.write("$\2\2\u01c4\u01c5\b@\5\2\u01c5\u0080\3\2\2\2\u01c6\u01c7")
        buf.write("\7v\2\2\u01c7\u01c8\7t\2\2\u01c8\u01c9\7w\2\2\u01c9\u01d0")
        buf.write("\7g\2\2\u01ca\u01cb\7h\2\2\u01cb\u01cc\7c\2\2\u01cc\u01cd")
        buf.write("\7n\2\2\u01cd\u01ce\7u\2\2\u01ce\u01d0\7g\2\2\u01cf\u01c6")
        buf.write("\3\2\2\2\u01cf\u01ca\3\2\2\2\u01d0\u0082\3\2\2\2\u01d1")
        buf.write("\u01d2\7p\2\2\u01d2\u01d3\7k\2\2\u01d3\u01d4\7n\2\2\u01d4")
        buf.write("\u0084\3\2\2\2\u01d5\u01d6\7\61\2\2\u01d6\u01d7\7\61\2")
        buf.write("\2\u01d7\u01db\3\2\2\2\u01d8\u01da\n\20\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01de\u01df\bC\6\2\u01df\u0086\3\2\2\2\u01e0\u01e1\7")
        buf.write("\61\2\2\u01e1\u01e2\7,\2\2\u01e2\u01e7\3\2\2\2\u01e3\u01e6")
        buf.write("\5\u0087D\2\u01e4\u01e6\13\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e7\u01e5\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01ea\u01eb\7,\2\2\u01eb\u01ec\7\61\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ee\bD\6\2\u01ee\u0088\3\2\2\2\u01ef")
        buf.write("\u01f1\t\21\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2\3\2\2")
        buf.write("\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4")
        buf.write("\3\2\2\2\u01f4\u01f5\bE\6\2\u01f5\u008a\3\2\2\2\u01f6")
        buf.write("\u01f7\13\2\2\2\u01f7\u01f8\bF\7\2\u01f8\u008c\3\2\2\2")
        buf.write("\u01f9\u0201\7$\2\2\u01fa\u0200\n\16\2\2\u01fb\u01fc\7")
        buf.write("^\2\2\u01fc\u0200\t\17\2\2\u01fd\u01fe\7)\2\2\u01fe\u0200")
        buf.write("\7$\2\2\u01ff\u01fa\3\2\2\2\u01ff\u01fb\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3")
        buf.write("\2\2\2\u0204\u0206\t\22\2\2\u0205\u0204\3\2\2\2\u0206")
        buf.write("\u0207\3\2\2\2\u0207\u0208\bG\b\2\u0208\u008e\3\2\2\2")
        buf.write("\u0209\u020a\t\17\2\2\u020a\u0090\3\2\2\2\u020b\u0213")
        buf.write("\7$\2\2\u020c\u0212\n\16\2\2\u020d\u020e\7^\2\2\u020e")
        buf.write("\u0212\t\17\2\2\u020f\u0210\7)\2\2\u0210\u0212\7$\2\2")
        buf.write("\u0211\u020c\3\2\2\2\u0211\u020d\3\2\2\2\u0211\u020f\3")
        buf.write("\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0216")
        buf.write("\u0217\7^\2\2\u0217\u0218\n\23\2\2\u0218\u0219\bI\t\2")
        buf.write("\u0219\u0092\3\2\2\2 \2\u0156\u015e\u0161\u0168\u0171")
        buf.write("\u017a\u0186\u018d\u0190\u0197\u019b\u01a1\u01a4\u01a9")
        buf.write("\u01ac\u01b3\u01b6\u01be\u01c0\u01cf\u01db\u01e5\u01e7")
        buf.write("\u01f2\u01ff\u0201\u0205\u0211\u0213\n\3\67\2\38\3\39")
        buf.write("\4\3@\5\b\2\2\3F\6\3G\7\3I\b")
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
    PLUS = 22
    MINUS = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    NOTEQUAL = 28
    LE = 29
    GE = 30
    LT = 31
    GT = 32
    AND = 33
    OR = 34
    NOT = 35
    PLUSEQ = 36
    MINUSEQ = 37
    MULEQ = 38
    DIVEQ = 39
    MODEQ = 40
    COLONEQ = 41
    ASSIGN = 42
    DOT = 43
    LPAREN = 44
    RPAREN = 45
    LBRACE = 46
    RBRACE = 47
    LBRACK = 48
    RBRACK = 49
    COMMA = 50
    SEMI = 51
    ID = 52
    DECIMAL_LIT = 53
    BINARY_LIT = 54
    OCT_LIT = 55
    HEXA_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    BOOLEAN_LIT = 59
    NIL_LIT = 60
    SINGLE_LINE_COMMENT = 61
    MULTI_LINE_COMMENT = 62
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    VALID_ESCAPES = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'true'", 
            "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'<='", "'>='", "'<'", "'>'", "'&&'", "'||'", "'!'", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "':='", "'='", "'.'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "EQUAL", "NOTEQUAL", "LE", "GE", "LT", "GT", "AND", 
            "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", "DIVEQ", "MODEQ", 
            "COLONEQ", "ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "LBRACK", "RBRACK", "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", 
            "OCT_LIT", "HEXA_LIT", "FLOAT_LIT", "STRING_LIT", "BOOLEAN_LIT", 
            "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "VALID_ESCAPES", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", 
                  "NOTEQUAL", "LE", "GE", "LT", "GT", "AND", "OR", "NOT", 
                  "PLUSEQ", "MINUSEQ", "MULEQ", "DIVEQ", "MODEQ", "COLONEQ", 
                  "ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "COMMA", "SEMI", "ID", "DECIMAL_LIT", 
                  "BINARY_LIT", "OCT_LIT", "HEXA_LIT", "HEX_DIGIT", "OCTAL_DIGIT", 
                  "BIN_DIGIT", "EXP", "FLOAT_LIT", "DECIMALS", "STRING_LIT", 
                  "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "VALID_ESCAPES", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[53] = self.BINARY_LIT_action 
            actions[54] = self.OCT_LIT_action 
            actions[55] = self.HEXA_LIT_action 
            actions[62] = self.STRING_LIT_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
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

     


