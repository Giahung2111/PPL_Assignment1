# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u026e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u009c\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\b\u00a3\n\b\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u00aa\n\t\3\n\3\n\3\n\3\n\5\n\u00b0\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00bf")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u00c8\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u00cf\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00db\n\22")
        buf.write("\f\22\16\22\u00de\13\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\7\23\u00e6\n\23\f\23\16\23\u00e9\13\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\7\24\u00f1\n\24\f\24\16\24\u00f4\13\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00fc\n\25\f\25\16")
        buf.write("\25\u00ff\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0107")
        buf.write("\n\26\f\26\16\26\u010a\13\26\3\27\3\27\3\27\5\27\u010f")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0121\n\30\3\30\7")
        buf.write("\30\u0124\n\30\f\30\16\30\u0127\13\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0130\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u013f")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u0145\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u014f\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0157\n\37\3\37\3\37\3\37\5")
        buf.write("\37\u015c\n\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\7!\u016e\n!\f!\16!\u0171\13!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\5\"\u017b\n\"\3\"\5\"\u017e\n\"\3\"\3")
        buf.write("\"\3\"\5\"\u0183\n\"\3#\3#\3#\3#\5#\u0189\n#\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\5$\u0192\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\5%\u019f\n%\3&\3&\3&\5&\u01a4\n&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\5\'\u01ae\n\'\3(\3(\3(\3(\3(\5(\u01b5")
        buf.write("\n(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01c2\n(\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01d1\n)\3*\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\5,\u01dc\n,\3,\3,\3,\5,\u01e1\n,\3")
        buf.write(",\3,\3,\3-\3-\3-\5-\u01e9\n-\3-\3-\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u01f6\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u0204\n\60\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\5\61\u020c\n\61\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u0213\n\62\3\63\3\63\5\63\u0217\n\63\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u0220\n\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u0230\n\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\3")
        buf.write("9\39\39\39\59\u0241\n9\3:\3:\5:\u0245\n:\3;\3;\3;\3;\5")
        buf.write(";\u024b\n;\3<\3<\3<\3<\5<\u0251\n<\3=\3=\3=\3=\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\5?\u0262\n?\3@\3@\3@\3@\3@\3")
        buf.write("@\5@\u026a\n@\3@\3@\3@\2\t\"$&(*.@A\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\2\n\3\2\27\30\3\29:\3\2 %\3")
        buf.write("\2\33\34\3\2\35\37\4\2\34\34((\3\2).\4\288EE\2\u0285\2")
        buf.write("\u0080\3\2\2\2\4\u008d\3\2\2\2\6\u008f\3\2\2\2\b\u0091")
        buf.write("\3\2\2\2\n\u0094\3\2\2\2\f\u009b\3\2\2\2\16\u00a2\3\2")
        buf.write("\2\2\20\u00a9\3\2\2\2\22\u00af\3\2\2\2\24\u00b1\3\2\2")
        buf.write("\2\26\u00b5\3\2\2\2\30\u00be\3\2\2\2\32\u00c0\3\2\2\2")
        buf.write("\34\u00c7\3\2\2\2\36\u00ce\3\2\2\2 \u00d0\3\2\2\2\"\u00d4")
        buf.write("\3\2\2\2$\u00df\3\2\2\2&\u00ea\3\2\2\2(\u00f5\3\2\2\2")
        buf.write("*\u0100\3\2\2\2,\u010e\3\2\2\2.\u0110\3\2\2\2\60\u012f")
        buf.write("\3\2\2\2\62\u0131\3\2\2\2\64\u0136\3\2\2\2\66\u013e\3")
        buf.write("\2\2\28\u0144\3\2\2\2:\u014e\3\2\2\2<\u0156\3\2\2\2>\u015d")
        buf.write("\3\2\2\2@\u0162\3\2\2\2B\u0172\3\2\2\2D\u0188\3\2\2\2")
        buf.write("F\u018a\3\2\2\2H\u0193\3\2\2\2J\u01a3\3\2\2\2L\u01a5\3")
        buf.write("\2\2\2N\u01af\3\2\2\2P\u01c3\3\2\2\2R\u01d2\3\2\2\2T\u01d5")
        buf.write("\3\2\2\2V\u01db\3\2\2\2X\u01e5\3\2\2\2Z\u01ec\3\2\2\2")
        buf.write("\\\u01f7\3\2\2\2^\u01fc\3\2\2\2`\u020b\3\2\2\2b\u0212")
        buf.write("\3\2\2\2d\u0216\3\2\2\2f\u0218\3\2\2\2h\u021f\3\2\2\2")
        buf.write("j\u0221\3\2\2\2l\u0224\3\2\2\2n\u0235\3\2\2\2p\u0240\3")
        buf.write("\2\2\2r\u0244\3\2\2\2t\u024a\3\2\2\2v\u0250\3\2\2\2x\u0252")
        buf.write("\3\2\2\2z\u0256\3\2\2\2|\u0261\3\2\2\2~\u0263\3\2\2\2")
        buf.write("\u0080\u0081\58\35\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2")
        buf.write("\2\u0083\u008e\5\n\6\2\u0084\u008e\5\32\16\2\u0085\u008e")
        buf.write("\7:\2\2\u0086\u008e\7=\2\2\u0087\u008e\7<\2\2\u0088\u008e")
        buf.write("\7;\2\2\u0089\u008e\7>\2\2\u008a\u008e\7?\2\2\u008b\u008e")
        buf.write("\5\6\4\2\u008c\u008e\7\26\2\2\u008d\u0083\3\2\2\2\u008d")
        buf.write("\u0084\3\2\2\2\u008d\u0085\3\2\2\2\u008d\u0086\3\2\2\2")
        buf.write("\u008d\u0087\3\2\2\2\u008d\u0088\3\2\2\2\u008d\u0089\3")
        buf.write("\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\5\3\2\2\2\u008f\u0090\t\2\2\2\u0090\7\3")
        buf.write("\2\2\2\u0091\u0092\5\22\n\2\u0092\u0093\5\30\r\2\u0093")
        buf.write("\t\3\2\2\2\u0094\u0095\5\b\5\2\u0095\u0096\7\63\2\2\u0096")
        buf.write("\u0097\5\f\7\2\u0097\u0098\7\64\2\2\u0098\13\3\2\2\2\u0099")
        buf.write("\u009c\5\16\b\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2")
        buf.write("\2\u009b\u009a\3\2\2\2\u009c\r\3\2\2\2\u009d\u009e\5\20")
        buf.write("\t\2\u009e\u009f\7\67\2\2\u009f\u00a0\5\16\b\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u00a3\5\20\t\2\u00a2\u009d\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\17\3\2\2\2\u00a4\u00aa\5\"\22\2\u00a5")
        buf.write("\u00a6\7\63\2\2\u00a6\u00a7\5\16\b\2\u00a7\u00a8\7\64")
        buf.write("\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a4\3\2\2\2\u00a9\u00a5")
        buf.write("\3\2\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\5\24\13\2\u00ac")
        buf.write("\u00ad\5\22\n\2\u00ad\u00b0\3\2\2\2\u00ae\u00b0\5\24\13")
        buf.write("\2\u00af\u00ab\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\23\3")
        buf.write("\2\2\2\u00b1\u00b2\7\65\2\2\u00b2\u00b3\t\3\2\2\u00b3")
        buf.write("\u00b4\7\66\2\2\u00b4\25\3\2\2\2\u00b5\u00b6\79\2\2\u00b6")
        buf.write("\27\3\2\2\2\u00b7\u00bf\7\16\2\2\u00b8\u00bf\7\17\2\2")
        buf.write("\u00b9\u00bf\7\20\2\2\u00ba\u00bf\7\r\2\2\u00bb\u00bf")
        buf.write("\7\f\2\2\u00bc\u00bf\5\26\f\2\u00bd\u00bf\5\b\5\2\u00be")
        buf.write("\u00b7\3\2\2\2\u00be\u00b8\3\2\2\2\u00be\u00b9\3\2\2\2")
        buf.write("\u00be\u00ba\3\2\2\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3")
        buf.write("\2\2\2\u00be\u00bd\3\2\2\2\u00bf\31\3\2\2\2\u00c0\u00c1")
        buf.write("\79\2\2\u00c1\u00c2\7\63\2\2\u00c2\u00c3\5\34\17\2\u00c3")
        buf.write("\u00c4\7\64\2\2\u00c4\33\3\2\2\2\u00c5\u00c8\5\36\20\2")
        buf.write("\u00c6\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3")
        buf.write("\2\2\2\u00c8\35\3\2\2\2\u00c9\u00ca\5 \21\2\u00ca\u00cb")
        buf.write("\7\67\2\2\u00cb\u00cc\5\36\20\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cf\5 \21\2\u00ce\u00c9\3\2\2\2\u00ce\u00cd\3\2\2\2")
        buf.write("\u00cf\37\3\2\2\2\u00d0\u00d1\79\2\2\u00d1\u00d2\7\3\2")
        buf.write("\2\u00d2\u00d3\5\"\22\2\u00d3!\3\2\2\2\u00d4\u00d5\b\22")
        buf.write("\1\2\u00d5\u00d6\5$\23\2\u00d6\u00dc\3\2\2\2\u00d7\u00d8")
        buf.write("\f\4\2\2\u00d8\u00d9\7\'\2\2\u00d9\u00db\5$\23\2\u00da")
        buf.write("\u00d7\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd#\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write("\2\u00df\u00e0\b\23\1\2\u00e0\u00e1\5&\24\2\u00e1\u00e7")
        buf.write("\3\2\2\2\u00e2\u00e3\f\4\2\2\u00e3\u00e4\7&\2\2\u00e4")
        buf.write("\u00e6\5&\24\2\u00e5\u00e2\3\2\2\2\u00e6\u00e9\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8%\3\2\2")
        buf.write("\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\b\24\1\2\u00eb\u00ec")
        buf.write("\5(\25\2\u00ec\u00f2\3\2\2\2\u00ed\u00ee\f\4\2\2\u00ee")
        buf.write("\u00ef\t\4\2\2\u00ef\u00f1\5(\25\2\u00f0\u00ed\3\2\2\2")
        buf.write("\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3")
        buf.write("\2\2\2\u00f3\'\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6")
        buf.write("\b\25\1\2\u00f6\u00f7\5*\26\2\u00f7\u00fd\3\2\2\2\u00f8")
        buf.write("\u00f9\f\4\2\2\u00f9\u00fa\t\5\2\2\u00fa\u00fc\5*\26\2")
        buf.write("\u00fb\u00f8\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fd\u00fe\3\2\2\2\u00fe)\3\2\2\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u0100\u0101\b\26\1\2\u0101\u0102\5,\27\2\u0102")
        buf.write("\u0108\3\2\2\2\u0103\u0104\f\4\2\2\u0104\u0105\t\6\2\2")
        buf.write("\u0105\u0107\5,\27\2\u0106\u0103\3\2\2\2\u0107\u010a\3")
        buf.write("\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109+")
        buf.write("\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\t\7\2\2\u010c")
        buf.write("\u010f\5,\27\2\u010d\u010f\5.\30\2\u010e\u010b\3\2\2\2")
        buf.write("\u010e\u010d\3\2\2\2\u010f-\3\2\2\2\u0110\u0111\b\30\1")
        buf.write("\2\u0111\u0112\5\60\31\2\u0112\u0125\3\2\2\2\u0113\u0114")
        buf.write("\f\6\2\2\u0114\u0115\7\65\2\2\u0115\u0116\5\"\22\2\u0116")
        buf.write("\u0117\7\66\2\2\u0117\u0124\3\2\2\2\u0118\u0119\f\5\2")
        buf.write("\2\u0119\u011a\7\60\2\2\u011a\u0124\79\2\2\u011b\u011c")
        buf.write("\f\4\2\2\u011c\u011d\7\60\2\2\u011d\u011e\79\2\2\u011e")
        buf.write("\u0120\7\61\2\2\u011f\u0121\5\f\7\2\u0120\u011f\3\2\2")
        buf.write("\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124")
        buf.write("\7\62\2\2\u0123\u0113\3\2\2\2\u0123\u0118\3\2\2\2\u0123")
        buf.write("\u011b\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126/\3\2\2\2\u0127\u0125\3\2\2")
        buf.write("\2\u0128\u0130\79\2\2\u0129\u0130\5\4\3\2\u012a\u0130")
        buf.write("\5\62\32\2\u012b\u012c\7\61\2\2\u012c\u012d\5\"\22\2\u012d")
        buf.write("\u012e\7\62\2\2\u012e\u0130\3\2\2\2\u012f\u0128\3\2\2")
        buf.write("\2\u012f\u0129\3\2\2\2\u012f\u012a\3\2\2\2\u012f\u012b")
        buf.write("\3\2\2\2\u0130\61\3\2\2\2\u0131\u0132\79\2\2\u0132\u0133")
        buf.write("\7\61\2\2\u0133\u0134\5\f\7\2\u0134\u0135\7\62\2\2\u0135")
        buf.write("\63\3\2\2\2\u0136\u0137\5\"\22\2\u0137\u0138\7\60\2\2")
        buf.write("\u0138\u0139\5\"\22\2\u0139\65\3\2\2\2\u013a\u013b\5:")
        buf.write("\36\2\u013b\u013c\5\66\34\2\u013c\u013f\3\2\2\2\u013d")
        buf.write("\u013f\3\2\2\2\u013e\u013a\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\67\3\2\2\2\u0140\u0141\5:\36\2\u0141\u0142\58\35")
        buf.write("\2\u0142\u0145\3\2\2\2\u0143\u0145\5:\36\2\u0144\u0140")
        buf.write("\3\2\2\2\u0144\u0143\3\2\2\2\u01459\3\2\2\2\u0146\u014f")
        buf.write("\5<\37\2\u0147\u014f\5V,\2\u0148\u014f\5> \2\u0149\u014f")
        buf.write("\5B\"\2\u014a\u014f\5J&\2\u014b\u014f\5R*\2\u014c\u014f")
        buf.write("\5T+\2\u014d\u014f\5X-\2\u014e\u0146\3\2\2\2\u014e\u0147")
        buf.write("\3\2\2\2\u014e\u0148\3\2\2\2\u014e\u0149\3\2\2\2\u014e")
        buf.write("\u014a\3\2\2\2\u014e\u014b\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014d\3\2\2\2\u014f;\3\2\2\2\u0150\u0157\5Z.\2")
        buf.write("\u0151\u0157\5\\/\2\u0152\u0157\5^\60\2\u0153\u0157\5")
        buf.write("l\67\2\u0154\u0157\5n8\2\u0155\u0157\5z>\2\u0156\u0150")
        buf.write("\3\2\2\2\u0156\u0151\3\2\2\2\u0156\u0152\3\2\2\2\u0156")
        buf.write("\u0153\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2")
        buf.write("\u0157\u015b\3\2\2\2\u0158\u015c\7E\2\2\u0159\u015c\7")
        buf.write("8\2\2\u015a\u015c\3\2\2\2\u015b\u0158\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015c=\3\2\2\2\u015d\u015e")
        buf.write("\5@!\2\u015e\u015f\t\b\2\2\u015f\u0160\5\"\22\2\u0160")
        buf.write("\u0161\t\t\2\2\u0161?\3\2\2\2\u0162\u0163\b!\1\2\u0163")
        buf.write("\u0164\79\2\2\u0164\u016f\3\2\2\2\u0165\u0166\f\5\2\2")
        buf.write("\u0166\u0167\7\65\2\2\u0167\u0168\5\"\22\2\u0168\u0169")
        buf.write("\7\66\2\2\u0169\u016e\3\2\2\2\u016a\u016b\f\4\2\2\u016b")
        buf.write("\u016c\7\60\2\2\u016c\u016e\79\2\2\u016d\u0165\3\2\2\2")
        buf.write("\u016d\u016a\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170A\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0173\7\4\2\2\u0173\u0174\7\61\2\2\u0174")
        buf.write("\u0175\5\"\22\2\u0175\u0176\7\62\2\2\u0176\u0177\7\63")
        buf.write("\2\2\u0177\u0178\5\66\34\2\u0178\u017a\7\64\2\2\u0179")
        buf.write("\u017b\5D#\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u017e\5F$\2\u017d\u017c\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0182\3\2\2\2\u017f\u0183\7E\2\2")
        buf.write("\u0180\u0183\78\2\2\u0181\u0183\3\2\2\2\u0182\u017f\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183C")
        buf.write("\3\2\2\2\u0184\u0185\5H%\2\u0185\u0186\5D#\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0189\5H%\2\u0188\u0184\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189E\3\2\2\2\u018a\u018b\7\5\2\2\u018b\u018c")
        buf.write("\7\63\2\2\u018c\u018d\5\66\34\2\u018d\u0191\7\64\2\2\u018e")
        buf.write("\u0192\7E\2\2\u018f\u0192\78\2\2\u0190\u0192\3\2\2\2\u0191")
        buf.write("\u018e\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0192G\3\2\2\2\u0193\u0194\7\5\2\2\u0194\u0195\7\4\2")
        buf.write("\2\u0195\u0196\7\61\2\2\u0196\u0197\5\"\22\2\u0197\u0198")
        buf.write("\7\62\2\2\u0198\u0199\7\63\2\2\u0199\u019a\5\66\34\2\u019a")
        buf.write("\u019e\7\64\2\2\u019b\u019f\7E\2\2\u019c\u019f\78\2\2")
        buf.write("\u019d\u019f\3\2\2\2\u019e\u019b\3\2\2\2\u019e\u019c\3")
        buf.write("\2\2\2\u019e\u019d\3\2\2\2\u019fI\3\2\2\2\u01a0\u01a4")
        buf.write("\5L\'\2\u01a1\u01a4\5N(\2\u01a2\u01a4\5P)\2\u01a3\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("K\3\2\2\2\u01a5\u01a6\7\6\2\2\u01a6\u01a7\5\"\22\2\u01a7")
        buf.write("\u01a8\7\63\2\2\u01a8\u01a9\5\66\34\2\u01a9\u01ad\7\64")
        buf.write("\2\2\u01aa\u01ae\7E\2\2\u01ab\u01ae\78\2\2\u01ac\u01ae")
        buf.write("\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01aeM\3\2\2\2\u01af\u01b4\7\6\2\2\u01b0")
        buf.write("\u01b5\5> \2\u01b1\u01b2\5Z.\2\u01b2\u01b3\78\2\2\u01b3")
        buf.write("\u01b5\3\2\2\2\u01b4\u01b0\3\2\2\2\u01b4\u01b1\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b7\5\"\22\2\u01b7\u01b8")
        buf.write("\78\2\2\u01b8\u01b9\5@!\2\u01b9\u01ba\t\b\2\2\u01ba\u01bb")
        buf.write("\5\"\22\2\u01bb\u01bc\7\63\2\2\u01bc\u01bd\5\66\34\2\u01bd")
        buf.write("\u01c1\7\64\2\2\u01be\u01c2\7E\2\2\u01bf\u01c2\78\2\2")
        buf.write("\u01c0\u01c2\3\2\2\2\u01c1\u01be\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c0\3\2\2\2\u01c2O\3\2\2\2\u01c3\u01c4")
        buf.write("\7\6\2\2\u01c4\u01c5\79\2\2\u01c5\u01c6\7\67\2\2\u01c6")
        buf.write("\u01c7\79\2\2\u01c7\u01c8\7.\2\2\u01c8\u01c9\7\25\2\2")
        buf.write("\u01c9\u01ca\5\"\22\2\u01ca\u01cb\7\63\2\2\u01cb\u01cc")
        buf.write("\5\66\34\2\u01cc\u01d0\7\64\2\2\u01cd\u01d1\7E\2\2\u01ce")
        buf.write("\u01d1\78\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01cd\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1Q\3\2\2")
        buf.write("\2\u01d2\u01d3\7\24\2\2\u01d3\u01d4\t\t\2\2\u01d4S\3\2")
        buf.write("\2\2\u01d5\u01d6\7\23\2\2\u01d6\u01d7\t\t\2\2\u01d7U\3")
        buf.write("\2\2\2\u01d8\u01d9\5@!\2\u01d9\u01da\7\60\2\2\u01da\u01dc")
        buf.write("\3\2\2\2\u01db\u01d8\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01de\79\2\2\u01de\u01e0\7\61\2\2")
        buf.write("\u01df\u01e1\5\f\7\2\u01e0\u01df\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\7\62\2\2\u01e3")
        buf.write("\u01e4\t\t\2\2\u01e4W\3\2\2\2\u01e5\u01e8\7\7\2\2\u01e6")
        buf.write("\u01e9\5\"\22\2\u01e7\u01e9\3\2\2\2\u01e8\u01e6\3\2\2")
        buf.write("\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\t\t\2\2\u01ebY\3\2\2\2\u01ec\u01ed\7\22\2\2\u01ed\u01f5")
        buf.write("\79\2\2\u01ee\u01ef\5\30\r\2\u01ef\u01f0\7/\2\2\u01f0")
        buf.write("\u01f1\5\"\22\2\u01f1\u01f6\3\2\2\2\u01f2\u01f3\7/\2\2")
        buf.write("\u01f3\u01f6\5\"\22\2\u01f4\u01f6\5\30\r\2\u01f5\u01ee")
        buf.write("\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("[\3\2\2\2\u01f7\u01f8\7\21\2\2\u01f8\u01f9\79\2\2\u01f9")
        buf.write("\u01fa\7/\2\2\u01fa\u01fb\5\"\22\2\u01fb]\3\2\2\2\u01fc")
        buf.write("\u01fd\7\b\2\2\u01fd\u01fe\79\2\2\u01fe\u01ff\7\61\2\2")
        buf.write("\u01ff\u0200\5`\61\2\u0200\u0203\7\62\2\2\u0201\u0204")
        buf.write("\5\30\r\2\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2\u0203")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\7\63\2")
        buf.write("\2\u0206\u0207\5\66\34\2\u0207\u0208\7\64\2\2\u0208_\3")
        buf.write("\2\2\2\u0209\u020c\5b\62\2\u020a\u020c\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020a\3\2\2\2\u020ca\3\2\2\2\u020d\u020e")
        buf.write("\5d\63\2\u020e\u020f\7\67\2\2\u020f\u0210\5b\62\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u0213\5d\63\2\u0212\u020d\3\2\2\2")
        buf.write("\u0212\u0211\3\2\2\2\u0213c\3\2\2\2\u0214\u0217\5f\64")
        buf.write("\2\u0215\u0217\5j\66\2\u0216\u0214\3\2\2\2\u0216\u0215")
        buf.write("\3\2\2\2\u0217e\3\2\2\2\u0218\u0219\5h\65\2\u0219\u021a")
        buf.write("\5\30\r\2\u021ag\3\2\2\2\u021b\u021c\79\2\2\u021c\u021d")
        buf.write("\7\67\2\2\u021d\u0220\5h\65\2\u021e\u0220\79\2\2\u021f")
        buf.write("\u021b\3\2\2\2\u021f\u021e\3\2\2\2\u0220i\3\2\2\2\u0221")
        buf.write("\u0222\79\2\2\u0222\u0223\5\30\r\2\u0223k\3\2\2\2\u0224")
        buf.write("\u0225\7\b\2\2\u0225\u0226\7\61\2\2\u0226\u0227\79\2\2")
        buf.write("\u0227\u0228\79\2\2\u0228\u0229\7\62\2\2\u0229\u022a\7")
        buf.write("9\2\2\u022a\u022b\7\61\2\2\u022b\u022c\5`\61\2\u022c\u022f")
        buf.write("\7\62\2\2\u022d\u0230\5\30\r\2\u022e\u0230\3\2\2\2\u022f")
        buf.write("\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230\u0231\3\2\2\2")
        buf.write("\u0231\u0232\7\63\2\2\u0232\u0233\58\35\2\u0233\u0234")
        buf.write("\7\64\2\2\u0234m\3\2\2\2\u0235\u0236\7\t\2\2\u0236\u0237")
        buf.write("\79\2\2\u0237\u0238\7\n\2\2\u0238\u0239\7\63\2\2\u0239")
        buf.write("\u023a\5p9\2\u023a\u023b\7\64\2\2\u023bo\3\2\2\2\u023c")
        buf.write("\u023d\5r:\2\u023d\u023e\5p9\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u0241\5r:\2\u0240\u023c\3\2\2\2\u0240\u023f\3\2\2\2\u0241")
        buf.write("q\3\2\2\2\u0242\u0245\5v<\2\u0243\u0245\5t;\2\u0244\u0242")
        buf.write("\3\2\2\2\u0244\u0243\3\2\2\2\u0245s\3\2\2\2\u0246\u0247")
        buf.write("\5l\67\2\u0247\u0248\5t;\2\u0248\u024b\3\2\2\2\u0249\u024b")
        buf.write("\5l\67\2\u024a\u0246\3\2\2\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("u\3\2\2\2\u024c\u024d\5x=\2\u024d\u024e\5v<\2\u024e\u0251")
        buf.write("\3\2\2\2\u024f\u0251\5x=\2\u0250\u024c\3\2\2\2\u0250\u024f")
        buf.write("\3\2\2\2\u0251w\3\2\2\2\u0252\u0253\79\2\2\u0253\u0254")
        buf.write("\5\30\r\2\u0254\u0255\t\t\2\2\u0255y\3\2\2\2\u0256\u0257")
        buf.write("\7\t\2\2\u0257\u0258\79\2\2\u0258\u0259\7\13\2\2\u0259")
        buf.write("\u025a\7\63\2\2\u025a\u025b\5|?\2\u025b\u025c\7\64\2\2")
        buf.write("\u025c{\3\2\2\2\u025d\u025e\5~@\2\u025e\u025f\5|?\2\u025f")
        buf.write("\u0262\3\2\2\2\u0260\u0262\5~@\2\u0261\u025d\3\2\2\2\u0261")
        buf.write("\u0260\3\2\2\2\u0262}\3\2\2\2\u0263\u0264\79\2\2\u0264")
        buf.write("\u0265\7\61\2\2\u0265\u0266\5`\61\2\u0266\u0269\7\62\2")
        buf.write("\2\u0267\u026a\5\30\r\2\u0268\u026a\3\2\2\2\u0269\u0267")
        buf.write("\3\2\2\2\u0269\u0268\3\2\2\2\u026a\u026b\3\2\2\2\u026b")
        buf.write("\u026c\t\t\2\2\u026c\177\3\2\2\2\66\u008d\u009b\u00a2")
        buf.write("\u00a9\u00af\u00be\u00c7\u00ce\u00dc\u00e7\u00f2\u00fd")
        buf.write("\u0108\u010e\u0120\u0123\u0125\u012f\u013e\u0144\u014e")
        buf.write("\u0156\u015b\u016d\u016f\u017a\u017d\u0182\u0188\u0191")
        buf.write("\u019e\u01a3\u01ad\u01b4\u01c1\u01d0\u01db\u01e0\u01e8")
        buf.write("\u01f5\u0203\u020b\u0212\u0216\u021f\u022f\u0240\u0244")
        buf.write("\u024a\u0250\u0261\u0269")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'str'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "<INVALID>", 
                     "'true'", "'false'", "'PutStringLn'", "'PutIntLn'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'", "'&&'", "'||'", "'!'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "':='", "'='", 
                     "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STR", "STRING", 
                      "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                      "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PUTSTRINGLN", 
                      "PUTINTLN", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "EQUAL", "NOTEQUAL", "LE", "GE", "LT", "GT", "AND", 
                      "OR", "NOT", "PLUSEQ", "MINUSEQ", "MULEQ", "DIVEQ", 
                      "MODEQ", "COLONEQ", "ASSIGN", "DOT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", 
                      "ID", "DECIMAL_LIT", "BINARY_LIT", "OCT_LIT", "HEXA_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "BOOLEAN_LIT", "NIL_LIT", 
                      "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "WS", 
                      "SEMICOLON_NEWLINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "VALID_ESCAPES", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_literal = 1
    RULE_bool_lit = 2
    RULE_type_array = 3
    RULE_array_lit = 4
    RULE_list_expression = 5
    RULE_list_expr = 6
    RULE_element_expr = 7
    RULE_dimension_dec_list = 8
    RULE_dimension_dec = 9
    RULE_type_struct = 10
    RULE_typ = 11
    RULE_struct_lit = 12
    RULE_list_elements = 13
    RULE_list_elem = 14
    RULE_element = 15
    RULE_expression = 16
    RULE_expression1 = 17
    RULE_expression2 = 18
    RULE_expression3 = 19
    RULE_expression4 = 20
    RULE_expression5 = 21
    RULE_expression6 = 22
    RULE_expression7 = 23
    RULE_function_call = 24
    RULE_method_call = 25
    RULE_nullable_statements_list = 26
    RULE_statements_list = 27
    RULE_statement = 28
    RULE_declaration_statement = 29
    RULE_assignment_statement = 30
    RULE_lhs = 31
    RULE_if_statement = 32
    RULE_list_else_if = 33
    RULE_else_statement = 34
    RULE_else_if = 35
    RULE_for_statement = 36
    RULE_basic_loop = 37
    RULE_ini_con_upd_loop = 38
    RULE_range_loop = 39
    RULE_break_statement = 40
    RULE_continue_statement = 41
    RULE_call_statement = 42
    RULE_return_statement = 43
    RULE_variables = 44
    RULE_constants = 45
    RULE_functions = 46
    RULE_paramaters_list = 47
    RULE_paramaters = 48
    RULE_paramater = 49
    RULE_associated_param = 50
    RULE_id_list = 51
    RULE_basic_param = 52
    RULE_methods = 53
    RULE_struct = 54
    RULE_struct_elements_list = 55
    RULE_struct_elements = 56
    RULE_method_list = 57
    RULE_fieldname_list = 58
    RULE_fieldname = 59
    RULE_interface = 60
    RULE_interface_method_list = 61
    RULE_interface_method = 62

    ruleNames =  [ "program", "literal", "bool_lit", "type_array", "array_lit", 
                   "list_expression", "list_expr", "element_expr", "dimension_dec_list", 
                   "dimension_dec", "type_struct", "typ", "struct_lit", 
                   "list_elements", "list_elem", "element", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "function_call", 
                   "method_call", "nullable_statements_list", "statements_list", 
                   "statement", "declaration_statement", "assignment_statement", 
                   "lhs", "if_statement", "list_else_if", "else_statement", 
                   "else_if", "for_statement", "basic_loop", "ini_con_upd_loop", 
                   "range_loop", "break_statement", "continue_statement", 
                   "call_statement", "return_statement", "variables", "constants", 
                   "functions", "paramaters_list", "paramaters", "paramater", 
                   "associated_param", "id_list", "basic_param", "methods", 
                   "struct", "struct_elements_list", "struct_elements", 
                   "method_list", "fieldname_list", "fieldname", "interface", 
                   "interface_method_list", "interface_method" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STR=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    NIL=20
    TRUE=21
    FALSE=22
    PUTSTRINGLN=23
    PUTINTLN=24
    PLUS=25
    MINUS=26
    MUL=27
    DIV=28
    MOD=29
    EQUAL=30
    NOTEQUAL=31
    LE=32
    GE=33
    LT=34
    GT=35
    AND=36
    OR=37
    NOT=38
    PLUSEQ=39
    MINUSEQ=40
    MULEQ=41
    DIVEQ=42
    MODEQ=43
    COLONEQ=44
    ASSIGN=45
    DOT=46
    LPAREN=47
    RPAREN=48
    LBRACE=49
    RBRACE=50
    LBRACK=51
    RBRACK=52
    COMMA=53
    SEMI=54
    ID=55
    DECIMAL_LIT=56
    BINARY_LIT=57
    OCT_LIT=58
    HEXA_LIT=59
    FLOAT_LIT=60
    STRING_LIT=61
    BOOLEAN_LIT=62
    NIL_LIT=63
    SINGLE_LINE_COMMENT=64
    MULTI_LINE_COMMENT=65
    WS=66
    SEMICOLON_NEWLINE=67
    ERROR_CHAR=68
    UNCLOSE_STRING=69
    VALID_ESCAPES=70
    ILLEGAL_ESCAPE=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.statements_list()
            self.state = 127
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def HEXA_LIT(self):
            return self.getToken(MiniGoParser.HEXA_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def BINARY_LIT(self):
            return self.getToken(MiniGoParser.BINARY_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_litContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.array_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.struct_lit()
                pass
            elif token in [MiniGoParser.DECIMAL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(MiniGoParser.DECIMAL_LIT)
                pass
            elif token in [MiniGoParser.HEXA_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(MiniGoParser.HEXA_LIT)
                pass
            elif token in [MiniGoParser.OCT_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.match(MiniGoParser.OCT_LIT)
                pass
            elif token in [MiniGoParser.BINARY_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.match(MiniGoParser.BINARY_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 136
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 137
                self.bool_lit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 138
                self.match(MiniGoParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = MiniGoParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_dec_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_dec_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_array" ):
                return visitor.visitType_array(self)
            else:
                return visitor.visitChildren(self)




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.dimension_dec_list()
            self.state = 144
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.type_array()
            self.state = 147
            self.match(MiniGoParser.LBRACE)
            self.state = 148
            self.list_expression()
            self.state = 149
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_expression)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACE, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEXA_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.list_expr()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Element_exprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_expr)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.element_expr()
                self.state = 156
                self.match(MiniGoParser.COMMA)
                self.state = 157
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.element_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = MiniGoParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_element_expr)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEXA_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.expression(0)
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(MiniGoParser.LBRACE)
                self.state = 164
                self.list_expr()
                self.state = 165
                self.match(MiniGoParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_dec_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_decContext,0)


        def dimension_dec_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_dec_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_dec_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_dec_list" ):
                return visitor.visitDimension_dec_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_dec_list(self):

        localctx = MiniGoParser.Dimension_dec_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimension_dec_list)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.dimension_dec()
                self.state = 170
                self.dimension_dec_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.dimension_dec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_dec" ):
                return visitor.visitDimension_dec(self)
            else:
                return visitor.visitChildren(self)




    def dimension_dec(self):

        localctx = MiniGoParser.Dimension_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dimension_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MiniGoParser.LBRACK)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.DECIMAL_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 177
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_struct" ):
                return visitor.visitType_struct(self)
            else:
                return visitor.visitChildren(self)




    def type_struct(self):

        localctx = MiniGoParser.Type_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def STR(self):
            return self.getToken(MiniGoParser.STR, 0)

        def type_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Type_structContext,0)


        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typ)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.STR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.match(MiniGoParser.STR)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.type_struct()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 7)
                self.state = 187
                self.type_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(MiniGoParser.ID)
            self.state = 191
            self.match(MiniGoParser.LBRACE)
            self.state = 192
            self.list_elements()
            self.state = 193
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_elem(self):
            return self.getTypedRuleContext(MiniGoParser.List_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements" ):
                return visitor.visitList_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_elements)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.list_elem()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elem(self):
            return self.getTypedRuleContext(MiniGoParser.List_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elem" ):
                return visitor.visitList_elem(self)
            else:
                return visitor.visitChildren(self)




    def list_elem(self):

        localctx = MiniGoParser.List_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_elem)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.element()
                self.state = 200
                self.match(MiniGoParser.COMMA)
                self.state = 201
                self.list_elem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MiniGoParser.ID)
            self.state = 207
            self.match(MiniGoParser.T__0)
            self.state = 208
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    self.match(MiniGoParser.OR)
                    self.state = 215
                    self.expression1(0) 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 224
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 225
                    self.match(MiniGoParser.AND)
                    self.state = 226
                    self.expression2(0) 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MiniGoParser.NOTEQUAL, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 235
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 236
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOTEQUAL) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GE) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.GT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 237
                    self.expression3(0) 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 246
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 247
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 248
                    self.expression4(0) 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 259
                    self.expression5() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEXA_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 273
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 274
                        self.match(MiniGoParser.LBRACK)
                        self.state = 275
                        self.expression(0)
                        self.state = 276
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 278
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 279
                        self.match(MiniGoParser.DOT)
                        self.state = 280
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 281
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 282
                        self.match(MiniGoParser.DOT)
                        self.state = 283
                        self.match(MiniGoParser.ID)
                        self.state = 284
                        self.match(MiniGoParser.LPAREN)
                        self.state = 286
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                        if la_ == 1:
                            self.state = 285
                            self.list_expression()


                        self.state = 288
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 294
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 295
                self.literal()
                pass

            elif la_ == 3:
                self.state = 296
                self.function_call()
                pass

            elif la_ == 4:
                self.state = 297
                self.match(MiniGoParser.LPAREN)
                self.state = 298
                self.expression(0)
                self.state = 299
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MiniGoParser.ID)
            self.state = 304
            self.match(MiniGoParser.LPAREN)
            self.state = 305
            self.list_expression()
            self.state = 306
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.expression(0)
            self.state = 309
            self.match(MiniGoParser.DOT)
            self.state = 310
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_statements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nullable_statements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_statements_list" ):
                return visitor.visitNullable_statements_list(self)
            else:
                return visitor.visitChildren(self)




    def nullable_statements_list(self):

        localctx = MiniGoParser.Nullable_statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_nullable_statements_list)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.statement()
                self.state = 313
                self.nullable_statements_list()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_list" ):
                return visitor.visitStatements_list(self)
            else:
                return visitor.visitChildren(self)




    def statements_list(self):

        localctx = MiniGoParser.Statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statements_list)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.statement()
                self.state = 319
                self.statements_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declaration_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.call_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 328
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 329
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 330
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 331
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(MiniGoParser.VariablesContext,0)


        def constants(self):
            return self.getTypedRuleContext(MiniGoParser.ConstantsContext,0)


        def functions(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionsContext,0)


        def methods(self):
            return self.getTypedRuleContext(MiniGoParser.MethodsContext,0)


        def struct(self):
            return self.getTypedRuleContext(MiniGoParser.StructContext,0)


        def interface(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceContext,0)


        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = MiniGoParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 334
                self.variables()
                pass

            elif la_ == 2:
                self.state = 335
                self.constants()
                pass

            elif la_ == 3:
                self.state = 336
                self.functions()
                pass

            elif la_ == 4:
                self.state = 337
                self.methods()
                pass

            elif la_ == 5:
                self.state = 338
                self.struct()
                pass

            elif la_ == 6:
                self.state = 339
                self.interface()
                pass


            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON_NEWLINE]:
                self.state = 342
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass
            elif token in [MiniGoParser.SEMI]:
                self.state = 343
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RBRACE, MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COLONEQ(self):
            return self.getToken(MiniGoParser.COLONEQ, 0)

        def PLUSEQ(self):
            return self.getToken(MiniGoParser.PLUSEQ, 0)

        def MINUSEQ(self):
            return self.getToken(MiniGoParser.MINUSEQ, 0)

        def MULEQ(self):
            return self.getToken(MiniGoParser.MULEQ, 0)

        def DIVEQ(self):
            return self.getToken(MiniGoParser.DIVEQ, 0)

        def MODEQ(self):
            return self.getToken(MiniGoParser.MODEQ, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.lhs(0)
            self.state = 348
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PLUSEQ) | (1 << MiniGoParser.MINUSEQ) | (1 << MiniGoParser.MULEQ) | (1 << MiniGoParser.DIVEQ) | (1 << MiniGoParser.MODEQ) | (1 << MiniGoParser.COLONEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 349
            self.expression(0)
            self.state = 350
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 363
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 355
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 356
                        self.match(MiniGoParser.LBRACK)
                        self.state = 357
                        self.expression(0)
                        self.state = 358
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 360
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 361
                        self.match(MiniGoParser.DOT)
                        self.state = 362
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def list_else_if(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_ifContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MiniGoParser.IF)
            self.state = 369
            self.match(MiniGoParser.LPAREN)
            self.state = 370
            self.expression(0)
            self.state = 371
            self.match(MiniGoParser.RPAREN)
            self.state = 372
            self.match(MiniGoParser.LBRACE)
            self.state = 373
            self.nullable_statements_list()
            self.state = 374
            self.match(MiniGoParser.RBRACE)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 375
                self.list_else_if()


            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 378
                self.else_statement()


            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON_NEWLINE]:
                self.state = 381
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass
            elif token in [MiniGoParser.SEMI]:
                self.state = 382
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RBRACE, MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def list_else_if(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_ifContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else_if" ):
                return visitor.visitList_else_if(self)
            else:
                return visitor.visitChildren(self)




    def list_else_if(self):

        localctx = MiniGoParser.List_else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_list_else_if)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.else_if()
                self.state = 387
                self.list_else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.else_if()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.ELSE)
            self.state = 393
            self.match(MiniGoParser.LBRACE)
            self.state = 394
            self.nullable_statements_list()
            self.state = 395
            self.match(MiniGoParser.RBRACE)
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 396
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass

            elif la_ == 2:
                self.state = 397
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 3:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MiniGoParser.ELSE)
            self.state = 402
            self.match(MiniGoParser.IF)
            self.state = 403
            self.match(MiniGoParser.LPAREN)
            self.state = 404
            self.expression(0)
            self.state = 405
            self.match(MiniGoParser.RPAREN)
            self.state = 406
            self.match(MiniGoParser.LBRACE)
            self.state = 407
            self.nullable_statements_list()
            self.state = 408
            self.match(MiniGoParser.RBRACE)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 409
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass

            elif la_ == 2:
                self.state = 410
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 3:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_loopContext,0)


        def ini_con_upd_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Ini_con_upd_loopContext,0)


        def range_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Range_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_statement)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.basic_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.ini_con_upd_loop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                self.range_loop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_loop" ):
                return visitor.visitBasic_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_loop(self):

        localctx = MiniGoParser.Basic_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_basic_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(MiniGoParser.FOR)
            self.state = 420
            self.expression(0)
            self.state = 421
            self.match(MiniGoParser.LBRACE)
            self.state = 422
            self.nullable_statements_list()
            self.state = 423
            self.match(MiniGoParser.RBRACE)
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON_NEWLINE]:
                self.state = 424
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass
            elif token in [MiniGoParser.SEMI]:
                self.state = 425
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RBRACE, MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ini_con_upd_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def COLONEQ(self):
            return self.getToken(MiniGoParser.COLONEQ, 0)

        def PLUSEQ(self):
            return self.getToken(MiniGoParser.PLUSEQ, 0)

        def MINUSEQ(self):
            return self.getToken(MiniGoParser.MINUSEQ, 0)

        def MULEQ(self):
            return self.getToken(MiniGoParser.MULEQ, 0)

        def DIVEQ(self):
            return self.getToken(MiniGoParser.DIVEQ, 0)

        def MODEQ(self):
            return self.getToken(MiniGoParser.MODEQ, 0)

        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def variables(self):
            return self.getTypedRuleContext(MiniGoParser.VariablesContext,0)


        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ini_con_upd_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIni_con_upd_loop" ):
                return visitor.visitIni_con_upd_loop(self)
            else:
                return visitor.visitChildren(self)




    def ini_con_upd_loop(self):

        localctx = MiniGoParser.Ini_con_upd_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ini_con_upd_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.FOR)
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 430
                self.assignment_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 431
                self.variables()
                self.state = 432
                self.match(MiniGoParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 436
            self.expression(0)
            self.state = 437
            self.match(MiniGoParser.SEMI)
            self.state = 438
            self.lhs(0)
            self.state = 439
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PLUSEQ) | (1 << MiniGoParser.MINUSEQ) | (1 << MiniGoParser.MULEQ) | (1 << MiniGoParser.DIVEQ) | (1 << MiniGoParser.MODEQ) | (1 << MiniGoParser.COLONEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 440
            self.expression(0)
            self.state = 441
            self.match(MiniGoParser.LBRACE)
            self.state = 442
            self.nullable_statements_list()
            self.state = 443
            self.match(MiniGoParser.RBRACE)
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON_NEWLINE]:
                self.state = 444
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass
            elif token in [MiniGoParser.SEMI]:
                self.state = 445
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RBRACE, MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLONEQ(self):
            return self.getToken(MiniGoParser.COLONEQ, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_loop" ):
                return visitor.visitRange_loop(self)
            else:
                return visitor.visitChildren(self)




    def range_loop(self):

        localctx = MiniGoParser.Range_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_range_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(MiniGoParser.FOR)
            self.state = 450
            self.match(MiniGoParser.ID)
            self.state = 451
            self.match(MiniGoParser.COMMA)
            self.state = 452
            self.match(MiniGoParser.ID)
            self.state = 453
            self.match(MiniGoParser.COLONEQ)
            self.state = 454
            self.match(MiniGoParser.RANGE)

            self.state = 455
            self.expression(0)
            self.state = 456
            self.match(MiniGoParser.LBRACE)
            self.state = 457
            self.nullable_statements_list()
            self.state = 458
            self.match(MiniGoParser.RBRACE)
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON_NEWLINE]:
                self.state = 459
                self.match(MiniGoParser.SEMICOLON_NEWLINE)
                pass
            elif token in [MiniGoParser.SEMI]:
                self.state = 460
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.RBRACE, MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(MiniGoParser.BREAK)
            self.state = 465
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.CONTINUE)
            self.state = 468
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 470
                self.lhs(0)
                self.state = 471
                self.match(MiniGoParser.DOT)


            self.state = 475
            self.match(MiniGoParser.ID)
            self.state = 476
            self.match(MiniGoParser.LPAREN)
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 477
                self.list_expression()


            self.state = 480
            self.match(MiniGoParser.RPAREN)
            self.state = 481
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.RETURN)
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEXA_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 484
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMI, MiniGoParser.SEMICOLON_NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 488
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = MiniGoParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(MiniGoParser.VAR)
            self.state = 491
            self.match(MiniGoParser.ID)
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 492
                self.typ()
                self.state = 493
                self.match(MiniGoParser.ASSIGN)
                self.state = 494
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 496
                self.match(MiniGoParser.ASSIGN)
                self.state = 497
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 498
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constants

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants" ):
                return visitor.visitConstants(self)
            else:
                return visitor.visitChildren(self)




    def constants(self):

        localctx = MiniGoParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_constants)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.CONST)
            self.state = 502
            self.match(MiniGoParser.ID)
            self.state = 503
            self.match(MiniGoParser.ASSIGN)
            self.state = 504
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramaters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Paramaters_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def nullable_statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nullable_statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = MiniGoParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.FUNC)
            self.state = 507
            self.match(MiniGoParser.ID)
            self.state = 508
            self.match(MiniGoParser.LPAREN)
            self.state = 509
            self.paramaters_list()
            self.state = 510
            self.match(MiniGoParser.RPAREN)
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STR, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 511
                self.typ()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 515
            self.match(MiniGoParser.LBRACE)
            self.state = 516
            self.nullable_statements_list()
            self.state = 517
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramaters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramaters(self):
            return self.getTypedRuleContext(MiniGoParser.ParamatersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramaters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamaters_list" ):
                return visitor.visitParamaters_list(self)
            else:
                return visitor.visitChildren(self)




    def paramaters_list(self):

        localctx = MiniGoParser.Paramaters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_paramaters_list)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.paramaters()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamatersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramater(self):
            return self.getTypedRuleContext(MiniGoParser.ParamaterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramaters(self):
            return self.getTypedRuleContext(MiniGoParser.ParamatersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramaters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamaters" ):
                return visitor.visitParamaters(self)
            else:
                return visitor.visitChildren(self)




    def paramaters(self):

        localctx = MiniGoParser.ParamatersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_paramaters)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.paramater()
                self.state = 524
                self.match(MiniGoParser.COMMA)
                self.state = 525
                self.paramaters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.paramater()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamaterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def associated_param(self):
            return self.getTypedRuleContext(MiniGoParser.Associated_paramContext,0)


        def basic_param(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_paramContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramater

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamater" ):
                return visitor.visitParamater(self)
            else:
                return visitor.visitChildren(self)




    def paramater(self):

        localctx = MiniGoParser.ParamaterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_paramater)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.associated_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.basic_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Associated_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_associated_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssociated_param" ):
                return visitor.visitAssociated_param(self)
            else:
                return visitor.visitChildren(self)




    def associated_param(self):

        localctx = MiniGoParser.Associated_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_associated_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.id_list()
            self.state = 535
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_id_list)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(MiniGoParser.ID)
                self.state = 538
                self.match(MiniGoParser.COMMA)
                self.state = 539
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_param" ):
                return visitor.visitBasic_param(self)
            else:
                return visitor.visitChildren(self)




    def basic_param(self):

        localctx = MiniGoParser.Basic_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_basic_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(MiniGoParser.ID)
            self.state = 544
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def paramaters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Paramaters_listContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Statements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = MiniGoParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_methods)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(MiniGoParser.FUNC)
            self.state = 547
            self.match(MiniGoParser.LPAREN)
            self.state = 548
            self.match(MiniGoParser.ID)
            self.state = 549
            self.match(MiniGoParser.ID)
            self.state = 550
            self.match(MiniGoParser.RPAREN)
            self.state = 551
            self.match(MiniGoParser.ID)
            self.state = 552
            self.match(MiniGoParser.LPAREN)
            self.state = 553
            self.paramaters_list()
            self.state = 554
            self.match(MiniGoParser.RPAREN)
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STR, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 555
                self.typ()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 559
            self.match(MiniGoParser.LBRACE)
            self.state = 560
            self.statements_list()
            self.state = 561
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_elements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elements_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct" ):
                return visitor.visitStruct(self)
            else:
                return visitor.visitChildren(self)




    def struct(self):

        localctx = MiniGoParser.StructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.match(MiniGoParser.TYPE)
            self.state = 564
            self.match(MiniGoParser.ID)
            self.state = 565
            self.match(MiniGoParser.STRUCT)
            self.state = 566
            self.match(MiniGoParser.LBRACE)
            self.state = 567
            self.struct_elements_list()
            self.state = 568
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementsContext,0)


        def struct_elements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elements_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elements_list" ):
                return visitor.visitStruct_elements_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_elements_list(self):

        localctx = MiniGoParser.Struct_elements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_struct_elements_list)
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.struct_elements()
                self.state = 571
                self.struct_elements_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.struct_elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldname_list(self):
            return self.getTypedRuleContext(MiniGoParser.Fieldname_listContext,0)


        def method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elements" ):
                return visitor.visitStruct_elements(self)
            else:
                return visitor.visitChildren(self)




    def struct_elements(self):

        localctx = MiniGoParser.Struct_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_struct_elements)
        try:
            self.state = 578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.fieldname_list()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
                self.method_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methods(self):
            return self.getTypedRuleContext(MiniGoParser.MethodsContext,0)


        def method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_list" ):
                return visitor.visitMethod_list(self)
            else:
                return visitor.visitChildren(self)




    def method_list(self):

        localctx = MiniGoParser.Method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_method_list)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.methods()
                self.state = 581
                self.method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.methods()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fieldname_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldname(self):
            return self.getTypedRuleContext(MiniGoParser.FieldnameContext,0)


        def fieldname_list(self):
            return self.getTypedRuleContext(MiniGoParser.Fieldname_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldname_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldname_list" ):
                return visitor.visitFieldname_list(self)
            else:
                return visitor.visitChildren(self)




    def fieldname_list(self):

        localctx = MiniGoParser.Fieldname_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_fieldname_list)
        try:
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.fieldname()
                self.state = 587
                self.fieldname_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 589
                self.fieldname()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldname" ):
                return visitor.visitFieldname(self)
            else:
                return visitor.visitChildren(self)




    def fieldname(self):

        localctx = MiniGoParser.FieldnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_fieldname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(MiniGoParser.ID)
            self.state = 593
            self.typ()
            self.state = 594
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface" ):
                return visitor.visitInterface(self)
            else:
                return visitor.visitChildren(self)




    def interface(self):

        localctx = MiniGoParser.InterfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_interface)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(MiniGoParser.TYPE)
            self.state = 597
            self.match(MiniGoParser.ID)
            self.state = 598
            self.match(MiniGoParser.INTERFACE)
            self.state = 599
            self.match(MiniGoParser.LBRACE)
            self.state = 600
            self.interface_method_list()
            self.state = 601
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_list" ):
                return visitor.visitInterface_method_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_list(self):

        localctx = MiniGoParser.Interface_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_interface_method_list)
        try:
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.interface_method()
                self.state = 604
                self.interface_method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.interface_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramaters_list(self):
            return self.getTypedRuleContext(MiniGoParser.Paramaters_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON_NEWLINE(self):
            return self.getToken(MiniGoParser.SEMICOLON_NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(MiniGoParser.ID)
            self.state = 610
            self.match(MiniGoParser.LPAREN)
            self.state = 611
            self.paramaters_list()
            self.state = 612
            self.match(MiniGoParser.RPAREN)
            self.state = 615
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STR, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 613
                self.typ()
                pass
            elif token in [MiniGoParser.SEMI, MiniGoParser.SEMICOLON_NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 617
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.SEMICOLON_NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        self._predicates[17] = self.expression1_sempred
        self._predicates[18] = self.expression2_sempred
        self._predicates[19] = self.expression3_sempred
        self._predicates[20] = self.expression4_sempred
        self._predicates[22] = self.expression6_sempred
        self._predicates[31] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




