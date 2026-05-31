import sys
from random import randint, seed

def solution(T):
    A = [(word, i) for i, word in enumerate(T)]

    max_l = 0
    for word in T:
        if len(word) > max_l:
            max_l = len(word)

    for pos in range(max_l - 1, -1, -1):
        buckets = [[] for _ in range(27)]

        for word, original_index in A:
            if pos >= len(word):
                bucket_idx = 26
            else:
                char = word[pos]
                bucket_idx = ord('z') - ord(char)

            buckets[bucket_idx].append((word, original_index))

        A = []
        for bucket in buckets:
            A.extend(bucket)

    max_dominance = 0
    for current_index, (word, original_index) in enumerate(A):
        index_difference = original_index - current_index
        if index_difference > max_dominance:
            max_dominance = index_difference

    return max_dominance


if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))
    
    seed(1)
    test_def = [
        (10, 5, 10, 6),
        (100, 5, 10, 88),
        (100, 20, 100, 91),
        (10000, 10, 30, 9901)
    ]
    
    passed_tests = 0
    for idx, (n, m_low, m_high, ans) in enumerate(test_def):
        print(f"Test {idx + 1}")
        words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
        result = solution(words)
        
        if result == ans:
            print("OK")
            passed_tests += 1
        else:
            print("Error!")
            
    print(f"Result: {passed_tests} / {len(test_def)}")
