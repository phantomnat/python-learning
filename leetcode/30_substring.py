import json

class Solution:
    def pp(self, obj):
        print(json.dumps(obj, indent=2))

    def findSubstring(self, s, words):
        ans = []

        words_data = {}
        # word_found_array = []
        # create words_data
        for word in words:
            # init
            if word not in words_data:
                words_data[word] = {
                    'begin': 0,
                    'idx': -1,
                    'process': True,
                    'times': 1,
                    'last_idx': -1
                }
            else:
                words_data[word]['times'] += 1

        self.pp(words_data)

        while True:
            is_all_found = True
            word_found_idx = {}
            word_found_array = []

            for word, wd in words_data.items():
                if not wd['process']:
                    word_found_array.append(wd['idx'])
                    continue

                if wd['times'] > 1:
                    # handle same words
                    wd['idx'] = s.find(word, wd['begin'])
                    if wd['idx'] == -1:
                        # we aren't gonna find any match substring
                        is_all_found = False
                        break
                    word_found_idx[wd['idx']] = word
                    word_found_array.append(wd['idx'])
                    wd['last_idx'] = wd['idx'] + len(word)
                    for j in range(wd['times'] - 1):
                        _idx = wd['idx'] = s.find(word, wd['last_idx'])
                        if _idx == -1:
                            # we aren't gonna find any match substring
                            is_all_found = False
                            break
                        word_found_idx[_idx] = word
                        word_found_array.append(_idx)
                        wd['last_idx'] = _idx + len(word)
                else:
                    wd['idx'] = s.find(word, wd['begin'])
                    word_found_idx[wd['idx']] = word
                    word_found_array.append(wd['idx'])

                if wd['idx'] == -1 or not is_all_found:
                    # we aren't gonna find any match substring
                    is_all_found = False
                    break

                # word match
                # set begin to idx + 1
                # wd['begin'] = wd['idx'] + 1

            # self.pp(word_found_idx)
            # self.pp(word_found_array)

            if not is_all_found:
                break

            word_found_array.sort()

            # all words match
            # check index of all matches
            all_words_matched = True
            begin_match_idx = word_found_array[0]
            next_idx = begin_match_idx + len(word_found_idx[begin_match_idx])
            for i in range(1, len(word_found_array)):
                word_idx = word_found_array[i]
                if word_idx != next_idx:
                    # word not match
                    all_words_matched = False
                    break
                next_idx = word_idx + len(word_found_idx[word_idx])

            if all_words_matched:
                ans.append(begin_match_idx)

            # else:
            #     # set process and begin
            #     print('next search', next_idx)
            #     for word, wd in words_data.items():
            #         wd['begin'] = next_idx
            #         wd['process'] = True
            # print('next search', begin_match_idx + 1)
            # set process and begin
            for word, wd in words_data.items():
                wd['begin'] = begin_match_idx + 1
                wd['process'] = True
            # else:
            #     # not match
            #     for word, wd in words_data.items():
            #         wd['begin'] = next_idx + 1
            #         wd['process'] = True

        return ans

if __name__ == '__main__':
    s = Solution()
    # print(s.findSubstring('barfoothefoobarman', ['foo', 'bar']))
    # print(s.findSubstring('barfoofoobarthefoobarman', ['foo', 'bar', 'the']))
    # print(s.findSubstring('barfoothfoobarthefoobarman', ['foo', 'bar', 'the']))
    # print(s.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","good"]))
    # print(s.findSubstring('aaaaaaaa', ["aa","aa","aa"]))
    # print(s.findSubstring('pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel', ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]))

    print(s.findSubstring('ababaab', ["ab","ba","ba"]))
