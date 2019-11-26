import gensim
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
# --------------------------------------------
#           word2vec
# --------------------------------------------
model = gensim.models.Word2Vec.load('/Users/atec/Desktop/hansol_crawling/model/w2v_thermalPaperList(688).model')
most_silmilar_word = model.most_similar(positive=['thermal', 'paper'], topn=100)
print(most_silmilar_word) #단어와 가장 가까운 단어
print('=========================1')

# print('---------------')
# org_arr = ['state', 'face', 'flange', 'housing', 'cover', 'applies', 'closing', 'psolution', 'set', 'core', 'bearing', 'tension', 'moves', 'members', 'guide', 'end', 'door', 'rotates', 'mark', 'backup', 'axis', 'pressing', 'cartridge', 'harness', 'stopper', 'conveyance', 'front', 'rotation', 'sides', 'openings', 'puttingaside', 'reliability', 'angle', 'projecting', 'sheet', 'arrow', 'positioning', 'therebetween', 'energizing', 'brake', 'takeup', 'downstream', 'load', 'orthogonal', 'actuator', 'urging', 'tip', 'swinging', 'performs', 'manner', 'rubber', 'operator', 'locking', 'pcopyright', 'cam', 'heads', 'fed', 'there', 'printhead', 'transmission', 'erasure', 'chute', 'opening', 'port', 'address', 'nearer', 'operating', 'controls', 'plane', 'motor', 'cutter', 'opens', 'tape', 'feeder', 'prints', 'pawl', 'fan', 'plain', 'ribbon', 'doubleside', 'holder', 'operation', 'step', 'wound', 'comprises', 'scratching', 'movement', 'mounting', 'press', 'discharge', 'constitution', 'center', 'carriage', 'payoff', 'device', 'rollers', 'home', 'clip', 'problem', 'columnar', 'contact', 'imagewise', 'ccd', 'insertion', 'edge', 'roll', 'rule', 'left', 'relative', 'button', 'deviation', 'rate', 'interlocking', 'idler', 'replacement', 'cassette', 'guides', 'pa', 'pproblem', 'delivery', 'parallel', 'round', 'distortion', 'closes', 'moving', 'steps', 'medium', 'margin', 'sensor', 'assembling', 'lid', 'outside', 'place', 'document', 'conjunction', 'opposite', 'fulcrum', 'hole', 'order', 'distance', 'apparatus', 'passage', 'slider', 'type', 'drive', 'programs', 'systems', 'interlock', 'diameters', 'pressure', 'meshing', 'relationship', 'transport', 'mechanisms', 'it', 'feeding', 'thereto', 'constitutionthe', 'paperholding', 'setting', 'test', 'stocker', 'start', 'portions', 'shaft', 'gear', 'procedure', 'letter', 'pickup', 'error', 'driving', 'electrification', 'drawing', 'recession', 'sheets', 'ejection', 'separation', 'irregularity', 'insert', 'frontward', 'arrangement', 'rack', 'length', 'lever', 'reverse', 'planet', 'limiter', 'bearings', 'winder', 'program', 'outer', 'inference', 'member', 'module', 'display', 'friction', 'densities', 'marks', 'loading', 'normality', 'tubes', 'baggage', 'notches', 'lens', 'jet', 'needs', 'microswitch', 'staining', 'shank', 'timings', 'damage', 'enables', 'path', 'pos', 'number', 'intervals', 'duplicate', 'readout', 'defects', 'exit', 'object', 'printable', 'groove', 'point', 'suitable', 'outlet', 'mode', 'circumference', 'revolves', 'tray', 'alloy', 'issue', 'crank', 'picture', 'instrument', 'return', 'wall', 'cutting', 'counterclockwise', 'shell', 'console', 'surfaceof', 'detects', 'intermediary', 'safety', 'bankbook', 'sector', 'subframe', 'generators', 'twocolor', 'users', 'determination', 'title', 'graph', 'sticking', 'whole', 'regulation', 'barcode', 'force', 'alarm', 'pinion', 'missetting', 'platens', 'capable', 'conveying', 'constitutionwhen', 'smoking', 'completes', 'width', 'gsm', 'supply', 'controller', 'engagement', 'cooperation', 'rolls', 'produce', 'storage', 'wheel', 'question', 'ridge', 'positions', 'construction', 'multicolor', 'disk', 'hand', 'papers', 'stand', 'switching', 'stores', 'lights', 'diameter', 'pumps', 'sensors', 'depth', 'receiving', 'strip', 'curl', 'cushion', 'sections', 'accuracy', 'embodiment', 'clutch', 'tansfer', 'drawer', 'foam', 'gap', 'receives', 'case', 'actuators', 'absence', 'tc', 'receipts', 'periphery', 'pin', 'selector', 'inlet', 'burn', 'form', 'springs', 'features', 'basis', 'scheme', 'speed', 'degradation', 'thereby', 'action', 'assembly', 'rest', 'changeover', 'deflection', 'shafts', 'embodiments', 'seat', 'copy', 'card', 'inferiority', 'braking', 'block', 'dotmatrix', 'space', 'detection', 'rows', 'abnormality', 'passing', 'printers', 'electricity', 'machine', 'half', 'strings', 'extracting', 'aid', 'mainframe', 'drawingout', 'transmits', 'dimension', 'sets', 'motion', 'timing', 'copies', 'shape', 'habit', 'lines', 'points', 'recycle', 'scrolls', 'blocks', 'cavity', 'yields', 'lapse', 'dotrow', 'means', 'inclination', 'conveyer', 'sublimation', 'environment', 'ridges', 'yupo', 'presses', 'images', 'colum', 'clearance', 'rotary', 'widths', 'factor', 'battery', 'flexo', 'cpu', 'attachment', 'paper', 'cycles', 'scans', 'shift', 'provision', 'relation', 'bar', 'height', 'spool', 'modes', 'class', 'distances', 'contacts', 'types', 'piston', 'purpose', 'person', 'utilization', 'incline', 'bracket', 'fact', 'drawn', 'raisingup', 'reading', 'media', 'ceramics', 'fax', 'cpu', 'winding', 'shrinkage', 'statement', 'array', 'receipt', 'facsimile', 'row', 'generation', 'screw', 'stencil', 'pocket', 'halfway', 'presenceabsence', 'mechanism', 'perforation', 'register', 'delay', 'documents', 'stock', 'columns', 'communication', 'passes', 'necessity', 'toner', 'blade', 'processing', 'printout', 'manuscript', 'quality', 'mulitply', 'result', 'cl', 'leaf', 'to', 'tm', 'life', 'outputs', 'impact', 'feed', 'sz', 'words', 'torque', 'microcomputer', 'xcoordinates', 'forward', 'spring', 'nar', 'grooves', 'itself', 'contents', 'screen', 'dm', 'sales', 'treatment', 'portion', 'possibility', 'projection', 'transportation', 'exposure', 'burr', 'cap', 'extent', 'roll', 'heatgenerating', 'interval', 'rearward', 'matrix', 'marking', 'enters', 'intensity', 'blackboard', 'signals']
# # new_arr = ['face', 'state', 'roll', 'conveyance', 'psolution', 'cartridge', 'ejection', 'bearing', 'closing', 'feeding', 'flange', 'tension', 'housing', 'move', 'set', 'cover', 'rotates', 'sheet', 'door', 'sides', 'orthogonal', 'moves', 'backup', 'printhead', 'notches', 'mark', 'bearings', 'performs', 'therebetween', 'guide', 'front', 'sensor', 'angle', 'operator', 'moving', 'heads', 'stopper', 'member', 'payoff', 'members', 'energizing', 'axis', 'applies', 'chute', 'harness', 'force', 'reliability', 'drawn', 'end', 'load', 'feed', 'pproblem', 'shaft', 'core', 'mechanism', 'projecting', 'erasure', 'problem', 'puttingaside', 'motor', 'rotation', 'comprises', 'opens', 'spring', 'device', 'locking', 'cutter', 'positioning', 'there', 'scratching', 'operating', 'fan', 'ribbon', 'heatsensitive', 'relationship', 'clip', 'normality', 'downstream', 'closes', 'operation', 'conjunction', 'mounting', 'transmission', 'path', 'medium', 'relative', 'slider', 'takeup', 'controls', 'job', 'left', 'openings', 'loading', 'fed', 'cam', 'enters', 'discharge', 'contact', 'drive', 'pcopyright', 'tip', 'rate', 'incline', 'burn', 'arrow', 'movement', 'pressing', 'brake', 'rollers', 'program', 'assembling', 'imagewise', 'cassette', 'transportation', 'plane', 'electrifying', 'detects', 'tape', 'ccd', 'carriage', 'duplicating', 'swinging', 'constitution', 'apparatus', 'limiter', 'constitutionthe', 'degradation', 'error', 'braking', 'actuators', 'disk', 'round', 'wound', 'prints', 'idler', 'intermediary', 'actuator', 'holder', 'pickup', 'opening', 'start', 'center', 'home', 'it', 'module', 'inference', 'multicolor', 'pa', 'presses', 'feeder', 'surfaceof', 'type', 'manner', 'paperfeeding', 'recycle', 'opposite', 'interlock', 'place', 'sheets', 'selfadaption', 'letter', 'pawl', 'procedure', 'press', 'alarm', 'rack', 'abnormality', 'capable', 'reservoir', 'scans', 'portions', 'order', 'vice', 'retraction', 'pinion', 'rubber', 'reverse', 'scrolls', 'mechanisms', 'arrangement', 'lid', 'missetting', 'transport', 'fulcrum', 'outside', 'separates', 'defects', 'delay', 'gear', 'distortion', 'number', 'margin', 'conveying', 'needs', 'columnar', 'parallel', 'receipts', 'setting', 'printofseal', 'electrification', 'papers', 'storage', 'test', 'interlocking', 'subframe', 'driving', 'plain', 'nearer', 'doubleside', 'hole', 'position', 'speed', 'issue', 'slack', 'relation', 'line', 'title', 'display', 'body', 'length', 'halfway', 'delivery', 'direction', 'width', 'bracket', 'port', 'platens', 'gsm', 'stores', 'densities', 'diameters', 'mode', 'controller', 'step', 'produce', 'detection', 'planet', 'sorting', 'grooves', 'advance', 'dimension', 'recession', 'read', 'cycles', 'object', 'thereto', 'core', 'damage', 'electricity', 'forward', 'edge', 'effects', 'enables', 'paper', 'crank', 'frontward', 'sublimation', 'programs', 'ceramics', 'inferiority', 'deviation', 'clutch', 'absence', 'assembly', 'counterclockwise', 'distance', 'printer', 'separation', 'steps', 'button', 'diameter', 'changeover', 'adhesivefree', 'consideration', 'passage', 'sensors', 'sales', 'regulation', 'switching', 'perpendicular', 'lever', 'section', 'erasing', 'passing', 'selector', 'receipt', 'versa', 'types', 'meshing', 'outputs', 'unit', 'injectors', 'tray', 'lens', 'shift', 'scanning', 'hand', 'paperholding', 'aims', 'pop', 'cells', 'construction', 'address', 'means', 'copy', 'alloy', 'irregularity', 'supply', 'winder', 'rule', 'outer', 'stock', 'encoder', 'eliminating', 'guides', 'spools', 'revolves', 'wall', 'cavity', 'proportion', 'cutting', 'ridges', 'inclination', 'rotary', 'decoder', 'twocolor', 'half', 'quantity', 'extent', 'upstream', 'outlet', 'receiving', 'springs', 'life', 'determination', 'cooperation', 'battery', 'jet', 'bankbook', 'systems', 'sector', 'damper', 'basis', 'pin', 'pumps', 'widths', 'point', 'communication', 'marks', 'mountless', 'array', 'seal', 'stocker', 'torque', 'event', 'case', 'rises', 'insertion', 'plastics', 'insert', 'exit', 'method', 'picture', 'container', 'houses', 'past', 'either', 'extending', 'safety', 'users', 'lights', 'yupo', 'dm', 'such', 'machine', 'xcoordinates', 'input', 'jamming', 'shank', 'laminate', 'recognize', 'tinter', 'folding', 'return', 'blur', 'media', 'document', 'instrument', 'thereby', 'ridge', 'while', 'rest', 'letting', 'prevent', 'assemblies', 'accuracy', 'deterioration', 'time', 'typing', 'space', 'graph', 'cpu', 'commodity', 'photoprinter', 'pressure', 'modes', 'deflection', 'twoply', 'driven', 'person', 'constitutionwhen', 'features', 'wheel', 'permit', 'capability', 'printer', 'action', 'rolls', 'location', 'contents', 'lines', 'recipient', 'stencil', 'contacts', 'innermost', 'acceleration', 'curl', 'images', 'inkjet', 'replacement', 'positions', 'stop', 'cushion', 'trouble', 'durability', 'purpose', 'automate', 'colum', 'characterbycharacter', 'documents', 'fixture', 'perforation', 'magazine', 'plurality', 'whereby', 'stand', 'fork', 'quantities', 'baggage', 'side', 'strings', 'trajectory', 'collar', 'engagement', 'clearance', 'signals', 'forgery', 'twolayer', 'ocr', 'strip', 'period', 'directions', 'deformation', 'facsimile', 'guidance', 'divider', 'elements', 'shafts', 'lapse', 'sink', 'mainframe', 'suitable', 'nar', 'block', 'appts', 'interference', 'blade', 'swing', 'flexo', 'bias', 'matrix', 'adherence', 'principle', 'columns', 'urging', 'friction', 'habit', 'intervals']
# for word in org_arr:
#     print(word,',', model.wv.vocab[word].count)
# print('---------------')

vocab = list(model.wv.vocab)
X = model[vocab]
print('=========================2')

tsne = TSNE(n_components=2) # 2차원
X_tsne = tsne.fit_transform(X)
print('=========================3')

# 100개의 단어에 대해서만 시각화 ------------
X_tsne = tsne.fit_transform(X[:500,:])
df = pd.DataFrame(X_tsne, index=vocab[:500], columns=['x', 'y'])
df.shape
print('=========================4')

# ----------------- 그림 그리기
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df['x'], df['y'])

for word, pos in df.iterrows():
#     print('------------')
#     print('단어:'+word)
#     print("%d" % (pos[0]))
#     print("%d" % (pos[1]))
#     print("%d" % (pos))
    ax.annotate(word, pos, fontsize=8)

plt.show()
print('=========================5')

