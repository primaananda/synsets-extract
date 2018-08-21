from output_validasi_using_matrix import synsets_manual
from output_validasi_kbbi import  synsets_validasi_kbbi
from output_lower import synsets_lower
from synsets_extraction import alt_gen


def f1_score(synsets_program, synset_manual):

    relevant_synset = 0
    retrieved_synsets_program = len(synsets_program)
    retrieved_synsets_manual = len(synset_manual)
    if retrieved_synsets_manual != retrieved_synsets_program:
        raise ValueError('A very specific bad thing happened.')
    count = 0
    for program, manual in zip(synsets_program, synset_manual):
        count += 1
        for x , y in zip(program, manual):
            if x == y:
                relevant_synset += 1
            else:
                print('kata ke - ', count, 'program ', program, 'manual ', manual)
    print()

    # for program, manual in zip(synsets_program, synset_manual):
    #     if program == manual:
    #         relevant_synset += 1
    #     else:
    #         print('synset yang tidak sama ', program)
    # print()

    count_program = 0
    for matriks in synsets_program:
        for synset1 in matriks:
            for syn in synset1:
                count_program += 1
    count_manual = 0
    for matriks2 in synset_manual:
        for synset2 in matriks2:
            for syn2 in synset2:
                count_manual += 1
    print('Jumlah synsets yang sama : ', relevant_synset)
    precision = relevant_synset/count_program
    recall = relevant_synset/count_manual
    f1score = 2 * precision*recall/(precision+recall)
    print('precision    : ', precision * 100)
    print('recall       : ', recall * 100)
    print('F1-Score       : ', f1score * 100)


if __name__ == '__main__':
    synsets_final = []

    synsets_final.append(alt_gen('ahad', open('datatest/data_test/1.json')))
    synsets_final.append(alt_gen('setanggi', open('datatest/data_test/2.json')))
    synsets_final.append(alt_gen('aborsi', open('datatest/data_test/3.json')))
    synsets_final.append(alt_gen('pekan', open('datatest/data_test/4.json')))
    synsets_final.append(alt_gen('lebu', open('datatest/data_test/5.json')))
    synsets_final.append(alt_gen('abu', open('datatest/data_test/6.json')))
    synsets_final.append(alt_gen('peci', open('datatest/data_test/7.json')))
    synsets_final.append(alt_gen('koran', open('datatest/data_test/8.json')))
    synsets_final.append(alt_gen('susur', open('datatest/data_test/9.json')))
    synsets_final.append(alt_gen('temu', open('datatest/data_test/10.json')))
    synsets_final.append(alt_gen('suar', open('datatest/data_test/11.json')))
    synsets_final.append(alt_gen('lilin', open('datatest/data_test/12.json')))
    synsets_final.append(alt_gen('sakat', open('datatest/data_test/13.json')))
    synsets_final.append(alt_gen('satwa', open('datatest/data_test/14.json')))
    synsets_final.append(alt_gen('binatang', open('datatest/data_test/15.json')))
    synsets_final.append(alt_gen('fiksi', open('datatest/data_test/16.json')))
    synsets_final.append(alt_gen('lamur', open('datatest/data_test/17.json')))
    synsets_final.append(alt_gen('radas', open('datatest/data_test/18.json')))
    synsets_final.append(alt_gen('persentase', open('datatest/data_test/19.json')))
    synsets_final.append(alt_gen('bandrek', open('datatest/data_test/20.json')))
    synsets_final.append(alt_gen('minggu', open('datatest/data_test/21.json')))
    synsets_final.append(alt_gen('esa', open('datatest/data_test/22.json')))
    synsets_final.append(alt_gen('pengguguran', open('datatest/data_test/23.json')))
    synsets_final.append(alt_gen('pasar', open('datatest/data_test/24.json')))
    synsets_final.append(alt_gen('rekan', open('datatest/data_test/25.json')))
    synsets_final.append(alt_gen('kopiah', open('datatest/data_test/26.json')))
    synsets_final.append(alt_gen('songkok', open('datatest/data_test/27.json')))
    synsets_final.append(alt_gen('parafin', open('datatest/data_test/28.json')))
    synsets_final.append(alt_gen('parasit', open('datatest/data_test/29.json')))
    synsets_final.append(alt_gen('serbat', open('datatest/data_test/30.json')))

    list_kata = ['ahad', 'setanggi', 'aborsi', 'pekan', 'lebu', 'abu', 'peci',
                 'koran', 'susur', 'temu', 'suar', 'lilin', 'sakat', 'satwa', 'binatang',
                 'fiksi', 'lamur', 'radas', 'presentase', 'bandrek', 'minggu',
                 'esa', 'pengguguran', 'pasar', 'rekan', 'kopiah', 'songkok', 'parafin',
                 'parasi', 'serbat']
    count = 0
    print('Synsets hasil program - synset manual(Gold Standard)')
    for x, y in zip(synsets_final, synsets_validasi_kbbi):
        count += 1
        print('Kata ke-',count , list_kata[count-1], '= ' ,x , ' - ', y)

    print()
    print('==============================')
    print('Nilai precision recall dan f1 score antara program dengan synset validasi dengan kbbi')
    print()
    count_program = 0
    for matriks in synsets_final:
        for synset1 in matriks:
            for syn in synset1:
                count_program += 1
    count_manual = 0
    for matriks2 in synsets_validasi_kbbi:
        for synset2 in matriks2:
            for syn2 in synset2:
                count_manual += 1

    print('Jumlah synsets program : ', count_program)
    print('Jumlah synsets manual : ', count_manual)
    f1_score(synsets_final, synsets_validasi_kbbi)
    print('==============================')

    print()
    print('==============================')
    print('Nilai precision recall dan f1 score antara manual 1 dengan synset validasi dengan kbbi')
    print()
    count_program = 0
    for matriks in synsets_manual:
        for synset1 in matriks:
            for syn in synset1:
                count_program += 1
    count_manual = 0
    for matriks2 in synsets_validasi_kbbi:
        for synset2 in matriks2:
            for syn2 in synset2:
                count_manual += 1

    print('Jumlah synsets program : ', count_program)
    print('Jumlah synsets manual : ', count_manual)
    f1_score(synsets_manual, synsets_validasi_kbbi)
    print('==============================')

    print()
    print('==============================')
    print('Nilai lower bound')
    print()
    count_program = 0
    for matriks in synsets_lower:
        for synset1 in matriks:
            for syn in synset1:
                count_program += 1
    count_manual = 0
    for matriks2 in synsets_validasi_kbbi:
        for synset2 in matriks2:
            for syn2 in synset2:
                count_manual += 1

    print('Jumlah synsets program : ', count_program)
    print('Jumlah synsets manual : ', count_manual)
    f1_score(synsets_lower, synsets_validasi_kbbi)
    print('==============================')

    #====================

    list_kata2 = ['abang', 'kakak', 'kakang', 'kangmas', 'mas', 'uda', 'abrasi',
                  'erosi', 'pengikisan', 'absen', 'bolos', 'mangkir', 'adidaya', 'adikuasa',
                  'adipati', 'bupati', 'tumenggung', 'adiraja', 'kaisar', 'maharaja',
                  'aduk', 'advokasi', 'pembelaan', 'apologi', 'pledoi', 'akomodasi', 'aksara',
                  'alwah', 'ampelas', 'amunisi', 'anekdot', 'angsuran', 'cicilan', 'kredit',
                  'anteng', 'antup', 'sengat', 'anyelir', 'arai', 'manggar', 'mayang', 'aras',
                  'arit', 'pengarsipan', 'arteri', 'nadi', 'pengasahan', 'asam', 'asan',
                  'asap', 'gas', 'atak', 'atensi', 'atlas', 'peta', 'atlet', 'olahragawan',
                  'atom', 'zarah', 'molekul', 'atrium', 'auditor', 'awan', 'gegana', 'bom',
                  'mega', 'awi', 'buluh', 'ayam', 'ayun', 'aba-aba']

    synset_dataset = []

    print()
    synset_dataset.append(alt_gen('abang', open('datatest/dataset/1.json')))
    synset_dataset.append(alt_gen('kakak', open('datatest/dataset/2.json')))
    synset_dataset.append(alt_gen('kakang', open('datatest/dataset/3.json')))
    synset_dataset.append(alt_gen('kangmas', open('datatest/dataset/4.json')))
    synset_dataset.append(alt_gen('mas', open('datatest/dataset/5.json')))
    synset_dataset.append(alt_gen('uda', open('datatest/dataset/6.json')))
    synset_dataset.append(alt_gen('abrasi', open('datatest/dataset/7.json')))
    synset_dataset.append(alt_gen('erosi', open('datatest/dataset/8.json')))
    synset_dataset.append(alt_gen('pengikisan', open('datatest/dataset/9.json')))
    synset_dataset.append(alt_gen('absen', open('datatest/dataset/10.json')))
    synset_dataset.append(alt_gen('bolos', open('datatest/dataset/11.json')))
    synset_dataset.append(alt_gen('mangkir', open('datatest/dataset/12.json')))
    synset_dataset.append(alt_gen('adidaya', open('datatest/dataset/13.json')))
    synset_dataset.append(alt_gen('adikuasa', open('datatest/dataset/14.json')))
    synset_dataset.append(alt_gen('adipati', open('datatest/dataset/15.json')))
    synset_dataset.append(alt_gen('bupati', open('datatest/dataset/16.json')))
    synset_dataset.append(alt_gen('tumenggung', open('datatest/dataset/17.json')))
    synset_dataset.append(alt_gen('adiraja', open('datatest/dataset/18.json')))
    synset_dataset.append(alt_gen('kaisar', open('datatest/dataset/19.json')))
    synset_dataset.append(alt_gen('maharaja', open('datatest/dataset/20.json')))
    synset_dataset.append(alt_gen('aduk', open('datatest/dataset/21.json')))
    synset_dataset.append(alt_gen('advokasi', open('datatest/dataset/22.json')))
    synset_dataset.append(alt_gen('pembelaan', open('datatest/dataset/23.json')))
    synset_dataset.append(alt_gen('apologi', open('datatest/dataset/24.json')))
    synset_dataset.append(alt_gen('pledoi', open('datatest/dataset/25.json')))
    synset_dataset.append(alt_gen('akomodasi', open('datatest/dataset/26.json')))
    synset_dataset.append(alt_gen('aksara', open('datatest/dataset/27.json')))
    synset_dataset.append(alt_gen('alwah', open('datatest/dataset/28.json')))
    synset_dataset.append(alt_gen('ampelas', open('datatest/dataset/29.json')))
    synset_dataset.append(alt_gen('amunisi', open('datatest/dataset/30.json')))
    synset_dataset.append(alt_gen('anekdot', open('datatest/dataset/31.json')))
    synset_dataset.append(alt_gen('angsuran', open('datatest/dataset/32.json')))
    synset_dataset.append(alt_gen('cicilan', open('datatest/dataset/33.json')))
    synset_dataset.append(alt_gen('kredit', open('datatest/dataset/34.json')))
    synset_dataset.append(alt_gen('anteng', open('datatest/dataset/35.json')))
    synset_dataset.append(alt_gen('antup', open('datatest/dataset/36.json')))
    synset_dataset.append(alt_gen('sengat', open('datatest/dataset/37.json')))
    synset_dataset.append(alt_gen('anyelir', open('datatest/dataset/38.json')))
    synset_dataset.append(alt_gen('arai', open('datatest/dataset/39.json')))
    synset_dataset.append(alt_gen('manggar', open('datatest/dataset/40.json')))
    synset_dataset.append(alt_gen('mayang', open('datatest/dataset/41.json')))
    synset_dataset.append(alt_gen('aras', open('datatest/dataset/42.json')))
    synset_dataset.append(alt_gen('arit', open('datatest/dataset/43.json')))
    synset_dataset.append(alt_gen('pengarsipan', open('datatest/dataset/44.json')))
    synset_dataset.append(alt_gen('arteri', open('datatest/dataset/45.json')))
    synset_dataset.append(alt_gen('nadi', open('datatest/dataset/46.json')))
    synset_dataset.append(alt_gen('pengasahan', open('datatest/dataset/47.json')))
    synset_dataset.append(alt_gen('asam', open('datatest/dataset/48.json')))
    synset_dataset.append(alt_gen('asan', open('datatest/dataset/49.json')))
    synset_dataset.append(alt_gen('asap', open('datatest/dataset/50.json')))
    synset_dataset.append(alt_gen('gas', open('datatest/dataset/51.json')))
    synset_dataset.append(alt_gen('atak', open('datatest/dataset/52.json')))
    synset_dataset.append(alt_gen('atensi', open('datatest/dataset/53.json')))
    synset_dataset.append(alt_gen('atlas', open('datatest/dataset/54.json')))
    synset_dataset.append(alt_gen('peta', open('datatest/dataset/55.json')))
    synset_dataset.append(alt_gen('atlet', open('datatest/dataset/56.json')))
    synset_dataset.append(alt_gen('olahragawan', open('datatest/dataset/57.json')))
    synset_dataset.append(alt_gen('atom', open('datatest/dataset/58.json')))
    synset_dataset.append(alt_gen('zarah', open('datatest/dataset/59.json')))
    synset_dataset.append(alt_gen('molekul', open('datatest/dataset/60.json')))
    synset_dataset.append(alt_gen('atrium', open('datatest/dataset/61.json')))
    synset_dataset.append(alt_gen('auditor', open('datatest/dataset/62a.json')))
    synset_dataset.append(alt_gen('awan', open('datatest/dataset/63.json')))
    synset_dataset.append(alt_gen('gegana', open('datatest/dataset/64.json')))
    synset_dataset.append(alt_gen('bom', open('datatest/dataset/65.json')))
    synset_dataset.append(alt_gen('mega', open('datatest/dataset/66.json')))
    synset_dataset.append(alt_gen('awi', open('datatest/dataset/67.json')))
    synset_dataset.append(alt_gen('buluh', open('datatest/dataset/68.json')))
    synset_dataset.append(alt_gen('ayam', open('datatest/dataset/69.json')))
    synset_dataset.append(alt_gen('ayun', open('datatest/dataset/70.json')))
    synset_dataset.append(alt_gen('aba-aba', open('datatest/dataset/71.json')))

    f = open('datatest/output.txt', 'w+')
    countd = 0
    for k in synset_dataset:
        output_synset = ('kata - ', list_kata2[countd], ' memiliki synset : ' ,k)
        f.write(str(output_synset) + '\n')
        countd += 1
    f.close()