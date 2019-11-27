from demo import FateadmApi
import time 

pd_id           = "118637"     #用户中心页可以查询到pd信息
pd_key          = "ytG5aG+0W1UhaJntDjk8goXUAEbAcTYE"
app_id          = "318637"     #开发者分成用的账号，在开发者中心可以查询到
app_key         = "TfPEWvFgDB6dOoJQjYZrm3QHl6aAQ1/N"
pred_type       = "30600"
api             = FateadmApi(app_id, app_key, pd_id, pd_key)
anser_list = []
time_1 = time.time()
for num_name in range(0,10):
    file_name   = str(num_name) + '.png'
    rsp         = api.PredictFromFile(pred_type, file_name)
    anser_list.append(rsp.pred_rsp.value)
print(anser_list)
time_2 = time.time() - time_1
print('平均用时%fs',time_2/10)
