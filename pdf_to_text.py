from operations import itemgetter
import pdfplumber

def check_bboxes(word, table_bbox):
    """
    Check whether word is inside a table bbox.
    """
    l = word['x0'], word['top'], word['x1'], word['bottom']
    r = table_bbox
    return l[0] > r[0] and l[1] > r[1] and l[2] < r[2] and l[3] < r[3]

with pdfplumber.open("example.pdf") as pdf:
    for page in pdf.pages:
        page.extract_text()
        tables = page.find_tables()
        table_bboxes = [i.bbox for i in tables]
        tables = [{'table': i.extract(), 'top': i.bbox[1]} for i in tables]
        non_table_words = [word for word in page.extract_words() if not any(
            [check_bboxes(word, table_bbox) for table_bbox in table_bboxes])]
        lines = []
        for cluster in pdfplumber.utils.cluster_objects(
                non_table_words + tables, itemgetter('top'), tolerance=5):
            if 'text' in cluster[0]:
                lines.append(' '.join([i['text'] for i in cluster]))
            elif 'table' in cluster[0]:
                lines.append(cluster[0]['table'])