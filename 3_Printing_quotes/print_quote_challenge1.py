# -*- encoding: utf-8 -*-

# 입력대신 딕션너리를 사용
# (key : 인용구를 말한 사람, value : 인용구)
quotation_dic = dict()
quotation_dic['Obi-Wan Kenobi'] = "These aren't the droids you're looking for"
quotation_dic['kimJeonghwan'] = 'Hi'

# 딕션너리에 저장된 인용구 모두 출력
for dic_key in quotation_dic.keys() :
    print (dic_key + ' says, ' + '\"' + quotation_dic[dic_key] + '.\"')
