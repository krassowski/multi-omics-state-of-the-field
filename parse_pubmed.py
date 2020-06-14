from datetime import datetime


def listify(x):
    if x is None:
        return []
    if not isinstance(x, list):
        return [x]
    return x


def extract_abstract(article):
    abstract = None
    if 'Abstract' in article:
        abstract = article['Abstract']
        if 'AbstractText' in abstract:
            abstract = abstract['AbstractText']
            try:
                if isinstance(abstract, list):
                    abstract = '\n\n'.join([
                        (
                            '\n'.join([piece.get('@Label', ''), piece.get('#text', '')])
                            if isinstance(piece, dict) else
                            piece
                        )
                        for piece in abstract
                    ])
            except Exception:
                print(abstract)
                raise
            if isinstance(abstract, dict):
                if '#text' in abstract:
                    abstract = abstract['#text']
                elif 'b' in abstract:
                    abstract = abstract['b']
                    # this is so weird formatting...
                    if '#text' in abstract:
                        abstract = abstract['#text']
                else:
                    print(abstract)
                    raise
        else:
            raise ValueError(f'Do not know how to find text in abstract {abstract}')
    else:
        abstract = None
    return abstract


def maybe_int(x):
    if x is not None:
        return int(x)


def maybe_month(month):
    return {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12,
    }.get(month)


def parse_date(date):
    if 'MedlineDate' in date:
        date = date['MedlineDate'].replace(' - ', '-').replace('Mar/Apr', 'Mar-Apr')
        if ' ' in date:
            year, months = date.split(' ')
            month = months.split('-')[0]
        else:
            year = date
            month = 'Jan'

        try:
            parts = dict(
                year=int(year),
                month=maybe_month(month),
                day=1
            )
        except Exception:
            print(date)
            raise
    else:
        parts = dict(
            year=int(date.get('Year')),
            month=maybe_month(date.get('Month')),
            day=maybe_int(date.get('Day'))
        )
    return datetime(
        **{
            key: value or 1
            for key, value in parts.items()
        }
    )


def parse_doi(elocation):
    if isinstance(elocation, dict):
        elocations = [elocation]
    else:
        elocations = elocation
    for elocation in elocations:
        if elocation['@EIdType'] == 'doi':
            return elocation['#text']
