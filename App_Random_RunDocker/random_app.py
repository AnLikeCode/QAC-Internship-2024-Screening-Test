from flask import Flask, render_template, request
import random

app = Flask(__name__)


#Trang web xuất hiện đầu tiên
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random_list', methods=['POST'])
def process():

    #FUNCTION_1
    def generate_random_list(n):
        list_random = random.sample(range(0,2**n), 2*n)
        k_random = random.randint(0,2**n - 1)
        return list_random, k_random

    #FUNCTION_2
    def binary_rearch(list_m, k_m):
        left = 0
        right = len(list_m) - 1
        step = 0
        while left <= right:
            mid = (left + right) // 2
            step += 1
            if list_m[mid] == k_m:
                return True, step, mid
            elif list_m[left] == k_m:
                return True, step, left
            elif list_m[right] == k_m:
                return True, step, right
            elif list_m[mid] < k_m:
                left = mid + 1
                right -= 1
            else:
                right = mid - 1
                left += 1
        return False, step, mid

    #FUNCTION_3
    def list_less_than_k(list_sorted, k_n):
        less_than_k = []
        step = 0
        if check_k:
            less_than_k = list_sorted[:position]
            step += 1
            return less_than_k, step
        else:
            if k_n > list_sorted[len(list_sorted) - 1]: # Xem k có lớn hơn phần tử lớn nhất trong List không
                step += 1
                less_than_k = list_sorted
            else:
                left = 0
                right = len(list_sorted) - 1
                while list_sorted[left] < k_n:
                    step += 1
                    mid = (left + right) // 2
                    if list_sorted[mid] < k_n:
                        less_than_k += list_sorted[left:mid + 1]
                        left = mid + 1
                    elif list_sorted[mid] > k_n:
                        right = mid - 1
                        if right < 0: break
        return less_than_k, step

    # Lấy giá trị n từ input
    m = int(request.form['n']) 
    #Lời gọi hàm và gán các giá trị
    list_n, k = generate_random_list(m)
    list_new = sorted(list_n)
    check_k, sobuoc, position  = binary_rearch(list_new, k)
    list_less, sobuoc_less = list_less_than_k(list_new, k)

    result = {
        'list_n': list_n,
        'k': k,
        'check_k': check_k,
        'sobuoc': sobuoc,
        'list_less': list_less,
        'sobuoc_less': sobuoc_less
    }
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, debug = True)