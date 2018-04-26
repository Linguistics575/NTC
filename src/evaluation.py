"""
Provides evaluation methods for OCR correction result.

    Author: Haobo Gu
    Date created: 04/24/2018
    Python version: 3.6.2
"""
import nltk
import src.wer as wer


def evaluate(result_string, gold_string, eval_method='wer'):
    """
    Evaluate system's performance using word error rate or rouge measurement.
    Use 'wer' and 'rouge' to specify which measurement you're going to use.
    :type result_string: str
    :type gold_string: str
    :type eval_method: str
    :rtype: float
    """
    if eval_method == 'wer':
        hyp_list = result_string.split()
        ref_list = gold_string.split()
        # print(word_list1, word_list2)
        eval_result = wer.calculate_wer(ref_list, hyp_list)

    return eval_result


# def evaluate_by_folder(result_folder, gold_folder, result_name_pattern, gold_name_pattern, eval_method='rouge'):
#     """
#     Evaluate system's performance using word error rate or rouge measurement.
#     All files in the folder will be read.
#     Use 'wer' and 'rouge' to specify which measurement you're going to use.
#     :type result_folder: str
#     :type gold_folder: str
#     :type eval_method: str
#     :rtype: dictionary
#     """
#     if eval_method == 'wer':
#         return 0
#         # hyp_list = result_string.split()
#         # ref_list = gold_string.split()
#         # # print(word_list1, word_list2)
#         # eval_result = wer.calculate_wer(ref_list, hyp_list)

#     return eval_result



"""
** NOT COMPLETED PART **
"""
def word_match_rate(result_string, gold_string, scope=10):
    """
    Calculate overall word match rate between result string and gold string.
    WMR is an evaluation measurement with considering order of the word in the sentence

    :type result_string: str
    :type gold_string: str
    :type scope: int
    :rtype: float
    """
    re_word_list = nltk.word_tokenize(result_string)
    gold_word_list = nltk.word_tokenize(gold_string)
    gold_len = len(gold_word_list)
    cur = 0  # cursor in gold word list
    for index, word in enumerate(re_word_list):
        # Get range of
        start_index = cur - scope if cur - scope >= 0 else 0
        end_index = cur + scope if cur + scope < gold_len else gold_len


# Test script
if __name__ == '__main__':
    hyp = 'This machine can wreck a nice beach'
    # ref = 'This great machine can recognize speech'
    ref = 'This machine can wreck a good beach'
    print(evaluate(hyp, ref, 'wer'))
