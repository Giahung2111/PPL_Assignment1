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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0216\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\7\64\u0151\n\64\f\64\16")
        buf.write("\64\u0154\13\64\3\65\3\65\3\65\7\65\u0159\n\65\f\65\16")
        buf.write("\65\u015c\13\65\5\65\u015e\n\65\3\66\3\66\3\66\6\66\u0163")
        buf.write("\n\66\r\66\16\66\u0164\3\66\3\66\3\67\3\67\3\67\6\67\u016c")
        buf.write("\n\67\r\67\16\67\u016d\3\67\3\67\38\38\38\68\u0175\n8")
        buf.write("\r8\168\u0176\38\38\39\39\3:\3:\3;\3;\3<\3<\5<\u0183\n")
        buf.write("<\3<\3<\3<\7<\u0188\n<\f<\16<\u018b\13<\5<\u018d\n<\3")
        buf.write("=\3=\3=\7=\u0192\n=\f=\16=\u0195\13=\3=\5=\u0198\n=\3")
        buf.write("=\3=\6=\u019c\n=\r=\16=\u019d\3=\5=\u01a1\n=\3=\6=\u01a4")
        buf.write("\n=\r=\16=\u01a5\3=\5=\u01a9\n=\3>\3>\3>\7>\u01ae\n>\f")
        buf.write(">\16>\u01b1\13>\5>\u01b3\n>\3?\3?\3?\3?\3?\3?\7?\u01bb")
        buf.write("\n?\f?\16?\u01be\13?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@")
        buf.write("\3@\5@\u01cc\n@\3A\3A\3A\3A\3B\3B\3B\3B\7B\u01d6\nB\f")
        buf.write("B\16B\u01d9\13B\3B\3B\3C\3C\3C\3C\3C\7C\u01e2\nC\fC\16")
        buf.write("C\u01e5\13C\3C\3C\3C\3C\3C\3D\6D\u01ed\nD\rD\16D\u01ee")
        buf.write("\3D\3D\3E\3E\3E\3F\3F\3F\3F\3F\3F\7F\u01fc\nF\fF\16F\u01ff")
        buf.write("\13F\3F\5F\u0202\nF\3F\3F\3G\3G\3H\3H\3H\3H\3H\3H\7H\u020e")
        buf.write("\nH\fH\16H\u0211\13H\3H\3H\3H\3H\3\u01e3\2I\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w\2y")
        buf.write(":{\2};\177<\u0081=\u0083>\u0085?\u0087@\u0089A\u008bB")
        buf.write("\u008dC\u008fD\3\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62;\4\2DDdd\4\2QQqq\4\2ZZzz\5\2\62;CHch\3\2\629")
        buf.write("\3\2\62\63\4\2GGgg\4\2--//\5\2\f\f$$^^\7\2$$^^ppttvv\4")
        buf.write("\2\f\f\17\17\5\2\13\f\16\17\"\"\3\3\f\f\7\2))^^ppttvv")
        buf.write("\2\u0230\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u0094\3\2\2\2\7\u0099\3\2\2")
        buf.write("\2\t\u009d\3\2\2\2\13\u00a4\3\2\2\2\r\u00a9\3\2\2\2\17")
        buf.write("\u00ae\3\2\2\2\21\u00b5\3\2\2\2\23\u00bf\3\2\2\2\25\u00c6")
        buf.write("\3\2\2\2\27\u00ca\3\2\2\2\31\u00d0\3\2\2\2\33\u00d8\3")
        buf.write("\2\2\2\35\u00de\3\2\2\2\37\u00e2\3\2\2\2!\u00eb\3\2\2")
        buf.write("\2#\u00f1\3\2\2\2%\u00f7\3\2\2\2\'\u00fb\3\2\2\2)\u0100")
        buf.write("\3\2\2\2+\u0106\3\2\2\2-\u0108\3\2\2\2/\u010a\3\2\2\2")
        buf.write("\61\u010c\3\2\2\2\63\u010e\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0113\3\2\2\29\u0116\3\2\2\2;\u0119\3\2\2\2=\u011c\3")
        buf.write("\2\2\2?\u011e\3\2\2\2A\u0120\3\2\2\2C\u0123\3\2\2\2E\u0126")
        buf.write("\3\2\2\2G\u0128\3\2\2\2I\u012b\3\2\2\2K\u012e\3\2\2\2")
        buf.write("M\u0131\3\2\2\2O\u0134\3\2\2\2Q\u0137\3\2\2\2S\u013a\3")
        buf.write("\2\2\2U\u013c\3\2\2\2W\u013e\3\2\2\2Y\u0140\3\2\2\2[\u0142")
        buf.write("\3\2\2\2]\u0144\3\2\2\2_\u0146\3\2\2\2a\u0148\3\2\2\2")
        buf.write("c\u014a\3\2\2\2e\u014c\3\2\2\2g\u014e\3\2\2\2i\u015d\3")
        buf.write("\2\2\2k\u015f\3\2\2\2m\u0168\3\2\2\2o\u0171\3\2\2\2q\u017a")
        buf.write("\3\2\2\2s\u017c\3\2\2\2u\u017e\3\2\2\2w\u0180\3\2\2\2")
        buf.write("y\u01a8\3\2\2\2{\u01b2\3\2\2\2}\u01b4\3\2\2\2\177\u01cb")
        buf.write("\3\2\2\2\u0081\u01cd\3\2\2\2\u0083\u01d1\3\2\2\2\u0085")
        buf.write("\u01dc\3\2\2\2\u0087\u01ec\3\2\2\2\u0089\u01f2\3\2\2\2")
        buf.write("\u008b\u01f5\3\2\2\2\u008d\u0205\3\2\2\2\u008f\u0207\3")
        buf.write("\2\2\2\u0091\u0092\7k\2\2\u0092\u0093\7h\2\2\u0093\4\3")
        buf.write("\2\2\2\u0094\u0095\7g\2\2\u0095\u0096\7n\2\2\u0096\u0097")
        buf.write("\7u\2\2\u0097\u0098\7g\2\2\u0098\6\3\2\2\2\u0099\u009a")
        buf.write("\7h\2\2\u009a\u009b\7q\2\2\u009b\u009c\7t\2\2\u009c\b")
        buf.write("\3\2\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7v\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\n\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\f")
        buf.write("\3\2\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7{\2\2\u00ab\u00ac")
        buf.write("\7r\2\2\u00ac\u00ad\7g\2\2\u00ad\16\3\2\2\2\u00ae\u00af")
        buf.write("\7u\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7e\2\2\u00b3\u00b4\7v\2\2\u00b4\20")
        buf.write("\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\22\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\24\3\2\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\26")
        buf.write("\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7v\2\2\u00cf\30")
        buf.write("\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7c\2\2\u00d6\u00d7\7p\2\2\u00d7\32\3\2\2\2\u00d8\u00d9")
        buf.write("\7e\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\34\3\2\2\2\u00de\u00df")
        buf.write("\7x\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7t\2\2\u00e1\36")
        buf.write("\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7g\2\2\u00ea \3")
        buf.write("\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7m\2\2\u00f0\"")
        buf.write("\3\2\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6\7g\2\2\u00f6$\3")
        buf.write("\2\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7n\2\2\u00fa&\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff(\3")
        buf.write("\2\2\2\u0100\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105\7g\2\2\u0105*\3")
        buf.write("\2\2\2\u0106\u0107\7-\2\2\u0107,\3\2\2\2\u0108\u0109\7")
        buf.write("/\2\2\u0109.\3\2\2\2\u010a\u010b\7,\2\2\u010b\60\3\2\2")
        buf.write("\2\u010c\u010d\7\61\2\2\u010d\62\3\2\2\2\u010e\u010f\7")
        buf.write("\'\2\2\u010f\64\3\2\2\2\u0110\u0111\7?\2\2\u0111\u0112")
        buf.write("\7?\2\2\u0112\66\3\2\2\2\u0113\u0114\7#\2\2\u0114\u0115")
        buf.write("\7?\2\2\u01158\3\2\2\2\u0116\u0117\7>\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118:\3\2\2\2\u0119\u011a\7@\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b<\3\2\2\2\u011c\u011d\7>\2\2\u011d>\3\2\2")
        buf.write("\2\u011e\u011f\7@\2\2\u011f@\3\2\2\2\u0120\u0121\7(\2")
        buf.write("\2\u0121\u0122\7(\2\2\u0122B\3\2\2\2\u0123\u0124\7~\2")
        buf.write("\2\u0124\u0125\7~\2\2\u0125D\3\2\2\2\u0126\u0127\7#\2")
        buf.write("\2\u0127F\3\2\2\2\u0128\u0129\7-\2\2\u0129\u012a\7?\2")
        buf.write("\2\u012aH\3\2\2\2\u012b\u012c\7/\2\2\u012c\u012d\7?\2")
        buf.write("\2\u012dJ\3\2\2\2\u012e\u012f\7,\2\2\u012f\u0130\7?\2")
        buf.write("\2\u0130L\3\2\2\2\u0131\u0132\7\61\2\2\u0132\u0133\7?")
        buf.write("\2\2\u0133N\3\2\2\2\u0134\u0135\7\'\2\2\u0135\u0136\7")
        buf.write("?\2\2\u0136P\3\2\2\2\u0137\u0138\7<\2\2\u0138\u0139\7")
        buf.write("?\2\2\u0139R\3\2\2\2\u013a\u013b\7?\2\2\u013bT\3\2\2\2")
        buf.write("\u013c\u013d\7\60\2\2\u013dV\3\2\2\2\u013e\u013f\7*\2")
        buf.write("\2\u013fX\3\2\2\2\u0140\u0141\7+\2\2\u0141Z\3\2\2\2\u0142")
        buf.write("\u0143\7}\2\2\u0143\\\3\2\2\2\u0144\u0145\7\177\2\2\u0145")
        buf.write("^\3\2\2\2\u0146\u0147\7]\2\2\u0147`\3\2\2\2\u0148\u0149")
        buf.write("\7_\2\2\u0149b\3\2\2\2\u014a\u014b\7.\2\2\u014bd\3\2\2")
        buf.write("\2\u014c\u014d\7=\2\2\u014df\3\2\2\2\u014e\u0152\t\2\2")
        buf.write("\2\u014f\u0151\t\3\2\2\u0150\u014f\3\2\2\2\u0151\u0154")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("h\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u015e\7\62\2\2\u0156")
        buf.write("\u015a\t\4\2\2\u0157\u0159\t\5\2\2\u0158\u0157\3\2\2\2")
        buf.write("\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3")
        buf.write("\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u0155")
        buf.write("\3\2\2\2\u015d\u0156\3\2\2\2\u015ej\3\2\2\2\u015f\u0160")
        buf.write("\7\62\2\2\u0160\u0162\t\6\2\2\u0161\u0163\5u;\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\b")
        buf.write("\66\2\2\u0167l\3\2\2\2\u0168\u0169\7\62\2\2\u0169\u016b")
        buf.write("\t\7\2\2\u016a\u016c\5s:\2\u016b\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\b\67\3\2\u0170n\3\2\2\2\u0171")
        buf.write("\u0172\7\62\2\2\u0172\u0174\t\b\2\2\u0173\u0175\5q9\2")
        buf.write("\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0174\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179")
        buf.write("\b8\4\2\u0179p\3\2\2\2\u017a\u017b\t\t\2\2\u017br\3\2")
        buf.write("\2\2\u017c\u017d\t\n\2\2\u017dt\3\2\2\2\u017e\u017f\t")
        buf.write("\13\2\2\u017fv\3\2\2\2\u0180\u0182\t\f\2\2\u0181\u0183")
        buf.write("\t\r\2\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183")
        buf.write("\u018c\3\2\2\2\u0184\u018d\7\62\2\2\u0185\u0189\t\4\2")
        buf.write("\2\u0186\u0188\t\5\2\2\u0187\u0186\3\2\2\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u0184\3\2\2\2")
        buf.write("\u018c\u0185\3\2\2\2\u018dx\3\2\2\2\u018e\u018f\5{>\2")
        buf.write("\u018f\u0193\7\60\2\2\u0190\u0192\t\5\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0196\u0198\5w<\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2")
        buf.write("\2\2\u0198\u01a9\3\2\2\2\u0199\u019b\7\60\2\2\u019a\u019c")
        buf.write("\t\5\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2")
        buf.write("\u019f\u01a1\5w<\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2")
        buf.write("\2\2\u01a1\u01a9\3\2\2\2\u01a2\u01a4\t\5\2\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a9\5w<\2\u01a8")
        buf.write("\u018e\3\2\2\2\u01a8\u0199\3\2\2\2\u01a8\u01a3\3\2\2\2")
        buf.write("\u01a9z\3\2\2\2\u01aa\u01b3\7\62\2\2\u01ab\u01af\t\4\2")
        buf.write("\2\u01ac\u01ae\t\5\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01aa\3\2\2\2")
        buf.write("\u01b2\u01ab\3\2\2\2\u01b3|\3\2\2\2\u01b4\u01bc\7$\2\2")
        buf.write("\u01b5\u01bb\n\16\2\2\u01b6\u01b7\7^\2\2\u01b7\u01bb\t")
        buf.write("\17\2\2\u01b8\u01b9\7)\2\2\u01b9\u01bb\7$\2\2\u01ba\u01b5")
        buf.write("\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\7")
        buf.write("$\2\2\u01c0\u01c1\b?\5\2\u01c1~\3\2\2\2\u01c2\u01c3\7")
        buf.write("v\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7w\2\2\u01c5\u01cc")
        buf.write("\7g\2\2\u01c6\u01c7\7h\2\2\u01c7\u01c8\7c\2\2\u01c8\u01c9")
        buf.write("\7n\2\2\u01c9\u01ca\7u\2\2\u01ca\u01cc\7g\2\2\u01cb\u01c2")
        buf.write("\3\2\2\2\u01cb\u01c6\3\2\2\2\u01cc\u0080\3\2\2\2\u01cd")
        buf.write("\u01ce\7p\2\2\u01ce\u01cf\7k\2\2\u01cf\u01d0\7n\2\2\u01d0")
        buf.write("\u0082\3\2\2\2\u01d1\u01d2\7\61\2\2\u01d2\u01d3\7\61\2")
        buf.write("\2\u01d3\u01d7\3\2\2\2\u01d4\u01d6\n\20\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01da\u01db\bB\6\2\u01db\u0084\3\2\2\2\u01dc\u01dd\7")
        buf.write("\61\2\2\u01dd\u01de\7,\2\2\u01de\u01e3\3\2\2\2\u01df\u01e2")
        buf.write("\5\u0085C\2\u01e0\u01e2\13\2\2\2\u01e1\u01df\3\2\2\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3")
        buf.write("\2\2\2\u01e6\u01e7\7,\2\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9")
        buf.write("\3\2\2\2\u01e9\u01ea\bC\6\2\u01ea\u0086\3\2\2\2\u01eb")
        buf.write("\u01ed\t\21\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2")
        buf.write("\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0")
        buf.write("\3\2\2\2\u01f0\u01f1\bD\6\2\u01f1\u0088\3\2\2\2\u01f2")
        buf.write("\u01f3\13\2\2\2\u01f3\u01f4\bE\7\2\u01f4\u008a\3\2\2\2")
        buf.write("\u01f5\u01fd\7$\2\2\u01f6\u01fc\n\16\2\2\u01f7\u01f8\7")
        buf.write("^\2\2\u01f8\u01fc\t\17\2\2\u01f9\u01fa\7)\2\2\u01fa\u01fc")
        buf.write("\7$\2\2\u01fb\u01f6\3\2\2\2\u01fb\u01f7\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2")
        buf.write("\u01fd\u01fe\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3")
        buf.write("\2\2\2\u0200\u0202\t\22\2\2\u0201\u0200\3\2\2\2\u0202")
        buf.write("\u0203\3\2\2\2\u0203\u0204\bF\b\2\u0204\u008c\3\2\2\2")
        buf.write("\u0205\u0206\t\17\2\2\u0206\u008e\3\2\2\2\u0207\u020f")
        buf.write("\7$\2\2\u0208\u020e\n\16\2\2\u0209\u020a\7^\2\2\u020a")
        buf.write("\u020e\t\17\2\2\u020b\u020c\7)\2\2\u020c\u020e\7$\2\2")
        buf.write("\u020d\u0208\3\2\2\2\u020d\u0209\3\2\2\2\u020d\u020b\3")
        buf.write("\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u020f\3\2\2\2\u0212")
        buf.write("\u0213\7^\2\2\u0213\u0214\n\23\2\2\u0214\u0215\bH\t\2")
        buf.write("\u0215\u0090\3\2\2\2 \2\u0152\u015a\u015d\u0164\u016d")
        buf.write("\u0176\u0182\u0189\u018c\u0193\u0197\u019d\u01a0\u01a5")
        buf.write("\u01a8\u01af\u01b2\u01ba\u01bc\u01cb\u01d7\u01e1\u01e3")
        buf.write("\u01ee\u01fb\u01fd\u0201\u020d\u020f\n\3\66\2\3\67\3\3")
        buf.write("8\4\3?\5\b\2\2\3E\6\3F\7\3H\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    PLUS = 21
    MINUS = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQUAL = 26
    NOTEQUAL = 27
    LE = 28
    GE = 29
    LT = 30
    GT = 31
    AND = 32
    OR = 33
    NOT = 34
    PLUSEQ = 35
    MINUSEQ = 36
    MULEQ = 37
    DIVEQ = 38
    MODEQ = 39
    COLONEQ = 40
    ASSIGN = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LBRACE = 45
    RBRACE = 46
    LBRACK = 47
    RBRACK = 48
    COMMA = 49
    SEMI = 50
    ID = 51
    DECIMAL_LIT = 52
    BINARY_LIT = 53
    OCT_LIT = 54
    HEXA_LIT = 55
    FLOAT_LIT = 56
    STRING_LIT = 57
    BOOLEAN_LIT = 58
    NIL_LIT = 59
    SINGLE_LINE_COMMENT = 60
    MULTI_LINE_COMMENT = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    VALID_ESCAPES = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
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

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", 
                  "LE", "GE", "LT", "GT", "AND", "OR", "NOT", "PLUSEQ", 
                  "MINUSEQ", "MULEQ", "DIVEQ", "MODEQ", "COLONEQ", "ASSIGN", 
                  "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "COMMA", "SEMI", "ID", "DECIMAL_LIT", "BINARY_LIT", 
                  "OCT_LIT", "HEXA_LIT", "HEX_DIGIT", "OCTAL_DIGIT", "BIN_DIGIT", 
                  "EXP", "FLOAT_LIT", "DECIMALS", "STRING_LIT", "BOOLEAN_LIT", 
                  "NIL_LIT", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
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
            actions[52] = self.BINARY_LIT_action 
            actions[53] = self.OCT_LIT_action 
            actions[54] = self.HEXA_LIT_action 
            actions[61] = self.STRING_LIT_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
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

     


