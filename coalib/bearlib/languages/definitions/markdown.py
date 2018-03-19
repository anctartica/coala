from coalib.bearlib.languages.Language import Language


@Language
class markdown:
    extensions = [
                    '.markdown','.mdown','.mkdn',
                    '.md', '.mkd','.mdwn','.mdtxt',
                    '.mdtext','.text','.Rmd']
    multiline_comment_delimiters = {'<!--': '-->'}
