import ul_finder
import unittest


class UlFinderTest(unittest.TestCase):

    def test_greatest_ul_1(self):
        self.assertEqual(ul_finder.greatest_ul(html_test_1), None)

    def test_greatest_ul_2(self):
        self.assertEqual(ul_finder.greatest_ul(html_test_2), {'ul': 1, 'has_li': 0})

    def test_greatest_ul_3(self):
        self.assertEqual(ul_finder.greatest_ul(html_test_3), {'ul': 2, 'has_li': 2})

    def test_greatest_ul_4(self):
        self.assertEqual(ul_finder.greatest_ul(html_test_4), {'ul': 2, 'has_li': 3})

    def test_greatest_ul_5(self):
        self.assertEqual(ul_finder.greatest_ul(html_test_5), {'ul': 2, 'has_li': 3})


html_test_1 = ('<!DOCTYPE html>'
               '<html lang="en">'
               '    <head>'
               '        <meta charset="UTF-8">'
               '        <title>Unordered lists</title>'
               '    </head>'
               '    <body>'
               '        <p>Some paragraph</p>'
               '    </body>'
               '</html>')

html_test_2 = ('<!DOCTYPE html>'
               '<html lang="en">'
               '    <head>'
               '        <meta charset="UTF-8">'
               '        <title>Unordered lists</title>'
               '    </head>'
               '    <body>'
               '        <p>Some paragraph</p>'
               '        <ul>'
               '        </ul>'
               '    </body>'
               '</html>')

html_test_3 = ('<!DOCTYPE html>'
               '<html lang="en">'
               '    <head>'
               '        <meta charset="UTF-8">'
               '        <title>Unordered lists</title>'
               '    </head>'
               '    <body>'
               '        <p>Some paragraph</p>'
               '        <ul>'
               '            <li>'
               '                <ul>'
               '                    <li>Element 1</li>'
               '                    <li>Last child 1</li>'
               '                </ul>'
               '            </li>'
               '            <li>Last child 1</li>'
               '        </ul>'
               '    </body>'
               '</html>')

html_test_4 = ('<!DOCTYPE html>'
               '<html lang="en">'
               '    <head>'
               '        <meta charset="UTF-8">'
               '        <title>Unordered lists</title>'
               '    </head>'
               '    <body>'
               '        <p>Some paragraph</p>'
               '        <ul>'
               '            <li>Element 1</li>'
               '            <li>'
               '                <ul>'
               '                    <li>Element 1</li>'
               '                    <li>Element 2</li>'
               '                    <li>Element 3</li>'
               '                </ul>'
               '            </li>'
               '        </ul>'
               '    </body>'
               '</html>')

html_test_5 = ('<!DOCTYPE html>'
               '<html lang="en">'
               '    <head>'
               '        <meta charset="UTF-8">'
               '        <title>Unordered lists</title>'
               '    </head>'
               '    <body>'
               '        <p>Some paragraph</p>'
               '        <ul>'
               '            <li>'
               '                <ul>'
               '                    <li>Element 1</li>'
               '                    <li>Element 2</li>'
               '                    <li>Element 3</li>'
               '                </ul>'
               '            </li>'
               '            <li>Element 1</li>'
               '        </ul>'
               '    </body>'
               '</html>')
