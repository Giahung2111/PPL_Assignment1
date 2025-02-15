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
        buf.write("\u0243\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\78\u0176\n8\f8\168\u0179")
        buf.write("\138\39\39\59\u017d\n9\39\39\39\79\u0182\n9\f9\169\u0185")
        buf.write("\139\59\u0187\n9\3:\3:\3:\6:\u018c\n:\r:\16:\u018d\3;")
        buf.write("\3;\3;\6;\u0193\n;\r;\16;\u0194\3<\3<\3<\6<\u019a\n<\r")
        buf.write("<\16<\u019b\3=\3=\3>\3>\3?\3?\3@\3@\5@\u01a6\n@\3@\3@")
        buf.write("\3@\7@\u01ab\n@\f@\16@\u01ae\13@\5@\u01b0\n@\3A\7A\u01b3")
        buf.write("\nA\fA\16A\u01b6\13A\3A\3A\7A\u01ba\nA\fA\16A\u01bd\13")
        buf.write("A\3A\5A\u01c0\nA\3A\3A\6A\u01c4\nA\rA\16A\u01c5\3A\5A")
        buf.write("\u01c9\nA\3A\6A\u01cc\nA\rA\16A\u01cd\3A\5A\u01d1\nA\3")
        buf.write("B\3B\3B\7B\u01d6\nB\fB\16B\u01d9\13B\5B\u01db\nB\3C\3")
        buf.write("C\3C\3C\3C\3C\7C\u01e3\nC\fC\16C\u01e6\13C\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\5D\u01f3\nD\3E\3E\3E\3E\3F\3F\3")
        buf.write("F\3F\7F\u01fd\nF\fF\16F\u0200\13F\3F\3F\3G\3G\3G\3G\3")
        buf.write("G\7G\u0209\nG\fG\16G\u020c\13G\3G\3G\3G\3G\3G\3H\6H\u0214")
        buf.write("\nH\rH\16H\u0215\3H\3H\3I\5I\u021b\nI\3I\3I\3I\3J\3J\3")
        buf.write("J\3K\3K\3K\3K\3K\3K\7K\u0229\nK\fK\16K\u022c\13K\3K\5")
        buf.write("K\u022f\nK\3K\3K\3L\3L\3M\3M\3M\3M\3M\3M\7M\u023b\nM\f")
        buf.write("M\16M\u023e\13M\3M\3M\3M\3M\3\u020a\2N\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177")
        buf.write("\2\u0081>\u0083\2\u0085?\u0087@\u0089A\u008bB\u008dC\u008f")
        buf.write("D\u0091E\u0093F\u0095G\u0097H\u0099I\3\2\24\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd\4\2QQqq\4\2Z")
        buf.write("Zzz\5\2\62;CHch\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2")
        buf.write("\f\f$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2\13\13\16\16\"")
        buf.write("\"\3\3\f\f\7\2))^^ppttvv\2\u0260\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009b")
        buf.write("\3\2\2\2\5\u009d\3\2\2\2\7\u00a0\3\2\2\2\t\u00a5\3\2\2")
        buf.write("\2\13\u00a9\3\2\2\2\r\u00b0\3\2\2\2\17\u00b5\3\2\2\2\21")
        buf.write("\u00ba\3\2\2\2\23\u00c1\3\2\2\2\25\u00cb\3\2\2\2\27\u00cf")
        buf.write("\3\2\2\2\31\u00d6\3\2\2\2\33\u00da\3\2\2\2\35\u00e0\3")
        buf.write("\2\2\2\37\u00e8\3\2\2\2!\u00ee\3\2\2\2#\u00f2\3\2\2\2")
        buf.write("%\u00fb\3\2\2\2\'\u0101\3\2\2\2)\u0107\3\2\2\2+\u010b")
        buf.write("\3\2\2\2-\u0110\3\2\2\2/\u0116\3\2\2\2\61\u0122\3\2\2")
        buf.write("\2\63\u012b\3\2\2\2\65\u012d\3\2\2\2\67\u012f\3\2\2\2")
        buf.write("9\u0131\3\2\2\2;\u0133\3\2\2\2=\u0135\3\2\2\2?\u0138\3")
        buf.write("\2\2\2A\u013b\3\2\2\2C\u013e\3\2\2\2E\u0141\3\2\2\2G\u0143")
        buf.write("\3\2\2\2I\u0145\3\2\2\2K\u0148\3\2\2\2M\u014b\3\2\2\2")
        buf.write("O\u014d\3\2\2\2Q\u0150\3\2\2\2S\u0153\3\2\2\2U\u0156\3")
        buf.write("\2\2\2W\u0159\3\2\2\2Y\u015c\3\2\2\2[\u015f\3\2\2\2]\u0161")
        buf.write("\3\2\2\2_\u0163\3\2\2\2a\u0165\3\2\2\2c\u0167\3\2\2\2")
        buf.write("e\u0169\3\2\2\2g\u016b\3\2\2\2i\u016d\3\2\2\2k\u016f\3")
        buf.write("\2\2\2m\u0171\3\2\2\2o\u0173\3\2\2\2q\u017c\3\2\2\2s\u0188")
        buf.write("\3\2\2\2u\u018f\3\2\2\2w\u0196\3\2\2\2y\u019d\3\2\2\2")
        buf.write("{\u019f\3\2\2\2}\u01a1\3\2\2\2\177\u01a3\3\2\2\2\u0081")
        buf.write("\u01d0\3\2\2\2\u0083\u01da\3\2\2\2\u0085\u01dc\3\2\2\2")
        buf.write("\u0087\u01f2\3\2\2\2\u0089\u01f4\3\2\2\2\u008b\u01f8\3")
        buf.write("\2\2\2\u008d\u0203\3\2\2\2\u008f\u0213\3\2\2\2\u0091\u021a")
        buf.write("\3\2\2\2\u0093\u021f\3\2\2\2\u0095\u0222\3\2\2\2\u0097")
        buf.write("\u0232\3\2\2\2\u0099\u0234\3\2\2\2\u009b\u009c\7<\2\2")
        buf.write("\u009c\4\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2")
        buf.write("\u009f\6\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2")
        buf.write("\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\b\3\2\2\2")
        buf.write("\u00a5\u00a6\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t")
        buf.write("\2\2\u00a8\n\3\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7")
        buf.write("g\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7p\2\2\u00af\f\3\2\2\2\u00b0\u00b1")
        buf.write("\7h\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7e\2\2\u00b4\16\3\2\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7{\2\2\u00b7\u00b8\7r\2\2\u00b8\u00b9\7g\2\2\u00b9\20")
        buf.write("\3\2\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\22\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9\u00ca\7g\2\2\u00ca\24\3\2\2\2\u00cb\u00cc")
        buf.write("\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\26")
        buf.write("\3\2\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5")
        buf.write("\7i\2\2\u00d5\30\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\32\3\2\2\2\u00da\u00db")
        buf.write("\7h\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7v\2\2\u00df\34\3\2\2\2\u00e0\u00e1")
        buf.write("\7d\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7n\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\36\3\2\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed \3\2\2\2\u00ee\u00ef\7x\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7t\2\2\u00f1\"\3\2\2\2\u00f2\u00f3")
        buf.write("\7e\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7v\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7w\2\2\u00f9\u00fa\7g\2\2\u00fa$\3\2\2\2\u00fb\u00fc")
        buf.write("\7d\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7m\2\2\u0100&\3\2\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7c\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7i\2\2\u0105\u0106\7g\2\2\u0106(\3\2\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7k\2\2\u0109\u010a\7n\2\2\u010a*\3")
        buf.write("\2\2\2\u010b\u010c\7v\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7w\2\2\u010e\u010f\7g\2\2\u010f,\3\2\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111\u0112\7c\2\2\u0112\u0113\7n\2\2\u0113\u0114")
        buf.write("\7u\2\2\u0114\u0115\7g\2\2\u0115.\3\2\2\2\u0116\u0117")
        buf.write("\7R\2\2\u0117\u0118\7w\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7U\2\2\u011a\u011b\7v\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f\7i\2\2\u011f\u0120")
        buf.write("\7N\2\2\u0120\u0121\7p\2\2\u0121\60\3\2\2\2\u0122\u0123")
        buf.write("\7R\2\2\u0123\u0124\7w\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7K\2\2\u0126\u0127\7p\2\2\u0127\u0128\7v\2\2\u0128\u0129")
        buf.write("\7N\2\2\u0129\u012a\7p\2\2\u012a\62\3\2\2\2\u012b\u012c")
        buf.write("\7-\2\2\u012c\64\3\2\2\2\u012d\u012e\7/\2\2\u012e\66\3")
        buf.write("\2\2\2\u012f\u0130\7,\2\2\u01308\3\2\2\2\u0131\u0132\7")
        buf.write("\61\2\2\u0132:\3\2\2\2\u0133\u0134\7\'\2\2\u0134<\3\2")
        buf.write("\2\2\u0135\u0136\7?\2\2\u0136\u0137\7?\2\2\u0137>\3\2")
        buf.write("\2\2\u0138\u0139\7#\2\2\u0139\u013a\7?\2\2\u013a@\3\2")
        buf.write("\2\2\u013b\u013c\7>\2\2\u013c\u013d\7?\2\2\u013dB\3\2")
        buf.write("\2\2\u013e\u013f\7@\2\2\u013f\u0140\7?\2\2\u0140D\3\2")
        buf.write("\2\2\u0141\u0142\7>\2\2\u0142F\3\2\2\2\u0143\u0144\7@")
        buf.write("\2\2\u0144H\3\2\2\2\u0145\u0146\7(\2\2\u0146\u0147\7(")
        buf.write("\2\2\u0147J\3\2\2\2\u0148\u0149\7~\2\2\u0149\u014a\7~")
        buf.write("\2\2\u014aL\3\2\2\2\u014b\u014c\7#\2\2\u014cN\3\2\2\2")
        buf.write("\u014d\u014e\7-\2\2\u014e\u014f\7?\2\2\u014fP\3\2\2\2")
        buf.write("\u0150\u0151\7/\2\2\u0151\u0152\7?\2\2\u0152R\3\2\2\2")
        buf.write("\u0153\u0154\7,\2\2\u0154\u0155\7?\2\2\u0155T\3\2\2\2")
        buf.write("\u0156\u0157\7\61\2\2\u0157\u0158\7?\2\2\u0158V\3\2\2")
        buf.write("\2\u0159\u015a\7\'\2\2\u015a\u015b\7?\2\2\u015bX\3\2\2")
        buf.write("\2\u015c\u015d\7<\2\2\u015d\u015e\7?\2\2\u015eZ\3\2\2")
        buf.write("\2\u015f\u0160\7?\2\2\u0160\\\3\2\2\2\u0161\u0162\7\60")
        buf.write("\2\2\u0162^\3\2\2\2\u0163\u0164\7*\2\2\u0164`\3\2\2\2")
        buf.write("\u0165\u0166\7+\2\2\u0166b\3\2\2\2\u0167\u0168\7}\2\2")
        buf.write("\u0168d\3\2\2\2\u0169\u016a\7\177\2\2\u016af\3\2\2\2\u016b")
        buf.write("\u016c\7]\2\2\u016ch\3\2\2\2\u016d\u016e\7_\2\2\u016e")
        buf.write("j\3\2\2\2\u016f\u0170\7.\2\2\u0170l\3\2\2\2\u0171\u0172")
        buf.write("\7=\2\2\u0172n\3\2\2\2\u0173\u0177\t\2\2\2\u0174\u0176")
        buf.write("\t\3\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178p\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017d\5\65\33\2\u017b\u017d\3\2\2")
        buf.write("\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u0186")
        buf.write("\3\2\2\2\u017e\u0187\7\62\2\2\u017f\u0183\t\4\2\2\u0180")
        buf.write("\u0182\t\5\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0187\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0186\u017e\3\2\2\2\u0186\u017f")
        buf.write("\3\2\2\2\u0187r\3\2\2\2\u0188\u0189\7\62\2\2\u0189\u018b")
        buf.write("\t\6\2\2\u018a\u018c\5}?\2\u018b\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("t\3\2\2\2\u018f\u0190\7\62\2\2\u0190\u0192\t\7\2\2\u0191")
        buf.write("\u0193\5{>\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195v\3\2\2\2\u0196")
        buf.write("\u0197\7\62\2\2\u0197\u0199\t\b\2\2\u0198\u019a\5y=\2")
        buf.write("\u0199\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019cx\3\2\2\2\u019d\u019e")
        buf.write("\t\t\2\2\u019ez\3\2\2\2\u019f\u01a0\t\n\2\2\u01a0|\3\2")
        buf.write("\2\2\u01a1\u01a2\t\13\2\2\u01a2~\3\2\2\2\u01a3\u01a5\t")
        buf.write("\f\2\2\u01a4\u01a6\t\r\2\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01af\3\2\2\2\u01a7\u01b0\7\62\2\2\u01a8")
        buf.write("\u01ac\t\4\2\2\u01a9\u01ab\t\5\2\2\u01aa\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01a7")
        buf.write("\3\2\2\2\u01af\u01a8\3\2\2\2\u01b0\u0080\3\2\2\2\u01b1")
        buf.write("\u01b3\t\5\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2")
        buf.write("\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3")
        buf.write("\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01bb\7\60\2\2\u01b8")
        buf.write("\u01ba\t\5\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bf\3")
        buf.write("\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c0\5\177@\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01d1\3\2\2\2")
        buf.write("\u01c1\u01c3\7\60\2\2\u01c2\u01c4\t\5\2\2\u01c3\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01c9\5\177@")
        buf.write("\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01d1")
        buf.write("\3\2\2\2\u01ca\u01cc\t\5\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d1\5\177@\2\u01d0\u01b4")
        buf.write("\3\2\2\2\u01d0\u01c1\3\2\2\2\u01d0\u01cb\3\2\2\2\u01d1")
        buf.write("\u0082\3\2\2\2\u01d2\u01db\7\62\2\2\u01d3\u01d7\t\4\2")
        buf.write("\2\u01d4\u01d6\t\5\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d9")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8")
        buf.write("\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01d2\3\2\2\2")
        buf.write("\u01da\u01d3\3\2\2\2\u01db\u0084\3\2\2\2\u01dc\u01e4\7")
        buf.write("$\2\2\u01dd\u01e3\n\16\2\2\u01de\u01df\7^\2\2\u01df\u01e3")
        buf.write("\t\17\2\2\u01e0\u01e1\7)\2\2\u01e1\u01e3\7$\2\2\u01e2")
        buf.write("\u01dd\3\2\2\2\u01e2\u01de\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8")
        buf.write("\7$\2\2\u01e8\u0086\3\2\2\2\u01e9\u01ea\7v\2\2\u01ea\u01eb")
        buf.write("\7t\2\2\u01eb\u01ec\7w\2\2\u01ec\u01f3\7g\2\2\u01ed\u01ee")
        buf.write("\7h\2\2\u01ee\u01ef\7c\2\2\u01ef\u01f0\7n\2\2\u01f0\u01f1")
        buf.write("\7u\2\2\u01f1\u01f3\7g\2\2\u01f2\u01e9\3\2\2\2\u01f2\u01ed")
        buf.write("\3\2\2\2\u01f3\u0088\3\2\2\2\u01f4\u01f5\7p\2\2\u01f5")
        buf.write("\u01f6\7k\2\2\u01f6\u01f7\7n\2\2\u01f7\u008a\3\2\2\2\u01f8")
        buf.write("\u01f9\7\61\2\2\u01f9\u01fa\7\61\2\2\u01fa\u01fe\3\2\2")
        buf.write("\2\u01fb\u01fd\n\20\2\2\u01fc\u01fb\3\2\2\2\u01fd\u0200")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0201\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0202\bF\2\2")
        buf.write("\u0202\u008c\3\2\2\2\u0203\u0204\7\61\2\2\u0204\u0205")
        buf.write("\7,\2\2\u0205\u020a\3\2\2\2\u0206\u0209\5\u008dG\2\u0207")
        buf.write("\u0209\13\2\2\2\u0208\u0206\3\2\2\2\u0208\u0207\3\2\2")
        buf.write("\2\u0209\u020c\3\2\2\2\u020a\u020b\3\2\2\2\u020a\u0208")
        buf.write("\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2\u020d")
        buf.write("\u020e\7,\2\2\u020e\u020f\7\61\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210\u0211\bG\2\2\u0211\u008e\3\2\2\2\u0212\u0214\t")
        buf.write("\21\2\2\u0213\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215")
        buf.write("\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0218\bH\2\2\u0218\u0090\3\2\2\2\u0219\u021b\7")
        buf.write("\17\2\2\u021a\u0219\3\2\2\2\u021a\u021b\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021c\u021d\7\f\2\2\u021d\u021e\bI\3\2")
        buf.write("\u021e\u0092\3\2\2\2\u021f\u0220\13\2\2\2\u0220\u0221")
        buf.write("\bJ\4\2\u0221\u0094\3\2\2\2\u0222\u022a\7$\2\2\u0223\u0229")
        buf.write("\n\16\2\2\u0224\u0225\7^\2\2\u0225\u0229\t\17\2\2\u0226")
        buf.write("\u0227\7)\2\2\u0227\u0229\7$\2\2\u0228\u0223\3\2\2\2\u0228")
        buf.write("\u0224\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022c\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022e\3")
        buf.write("\2\2\2\u022c\u022a\3\2\2\2\u022d\u022f\t\22\2\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231\bK\5\2")
        buf.write("\u0231\u0096\3\2\2\2\u0232\u0233\t\17\2\2\u0233\u0098")
        buf.write("\3\2\2\2\u0234\u023c\7$\2\2\u0235\u023b\n\16\2\2\u0236")
        buf.write("\u0237\7^\2\2\u0237\u023b\t\17\2\2\u0238\u0239\7)\2\2")
        buf.write("\u0239\u023b\7$\2\2\u023a\u0235\3\2\2\2\u023a\u0236\3")
        buf.write("\2\2\2\u023a\u0238\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023f\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023f\u0240\7^\2\2\u0240\u0241\n\23\2\2")
        buf.write("\u0241\u0242\bM\6\2\u0242\u009a\3\2\2\2#\2\u0177\u017c")
        buf.write("\u0183\u0186\u018d\u0194\u019b\u01a5\u01ac\u01af\u01b4")
        buf.write("\u01bb\u01bf\u01c5\u01c8\u01cd\u01d0\u01d7\u01da\u01e2")
        buf.write("\u01e4\u01f2\u01fe\u0208\u020a\u0215\u021a\u0228\u022a")
        buf.write("\u022e\u023a\u023c\7\b\2\2\3I\2\3J\3\3K\4\3M\5")
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
    STR = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    NIL = 20
    TRUE = 21
    FALSE = 22
    PUTSTRINGLN = 23
    PUTINTLN = 24
    PLUS = 25
    MINUS = 26
    MUL = 27
    DIV = 28
    MOD = 29
    EQUAL = 30
    NOTEQUAL = 31
    LE = 32
    GE = 33
    LT = 34
    GT = 35
    AND = 36
    OR = 37
    NOT = 38
    PLUSEQ = 39
    MINUSEQ = 40
    MULEQ = 41
    DIVEQ = 42
    MODEQ = 43
    COLONEQ = 44
    ASSIGN = 45
    DOT = 46
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
    SEMICOLON_NEWLINE = 67
    ERROR_CHAR = 68
    UNCLOSE_STRING = 69
    VALID_ESCAPES = 70
    ILLEGAL_ESCAPE = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'str'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'true'", "'false'", "'PutStringLn'", "'PutIntLn'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'=='", "'!='", "'<='", "'>='", "'<'", 
            "'>'", "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "':='", "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STR", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PUTSTRINGLN", 
            "PUTINTLN", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", 
            "LE", "GE", "LT", "GT", "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", 
            "MULEQ", "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", 
            "ID", "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", "HEXA_LIT", "FLOAT_LIT", 
            "STRING_LIT", "BOOLEAN_LIT", "NIL_LIT", "SINGLE_LINE_COMMENT", 
            "MULTI_LINE_COMMENT", "WS", "SEMICOLON_NEWLINE", "ERROR_CHAR", 
            "UNCLOSE_STRING", "VALID_ESCAPES", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STR", "STRING", "INT", "FLOAT", 
                  "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                  "NIL", "TRUE", "FALSE", "PUTSTRINGLN", "PUTINTLN", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LE", 
                  "GE", "LT", "GT", "AND", "OR", "NOT", "PLUSEQ", "MINUSEQ", 
                  "MULEQ", "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", "DOT", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", 
                  "HEXA_LIT", "HEX_DIGIT", "OCTAL_DIGIT", "BIN_DIGIT", "EXP", 
                  "FLOAT_LIT", "DECIMALS", "STRING_LIT", "BOOLEAN_LIT", 
                  "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                  "WS", "SEMICOLON_NEWLINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "VALID_ESCAPES", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
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
            actions[71] = self.SEMICOLON_NEWLINE_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def SEMICOLON_NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.preType in {self.ID, self.DECIMAL_LIT, self.TRUE,self.FALSE, self.STRING_LIT, self.FLOAT_LIT, 
                            self.RETURN, self.CONTINUE, self.BREAK,
                            self.RPAREN, self.RBRACK, self.RBRACE }:
                    self.text = ';'
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[0:-2]) 
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[0:-1]) 
                else:
                    raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                VAL_ESCAPES = ['n', 't', 'r', '"', '\\']
                for i in range(1, len(self.text)-1):
                    if self.text[i] == '\\' and self.text[i+1] not in VAL_ESCAPES:
                        raise IllegalEscape(self.text[0:i+2])

     


