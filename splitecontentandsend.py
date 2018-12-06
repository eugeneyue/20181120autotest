# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
#
# import tkinter.messagebox
# import time,random,smtplib,datetime
#
# qd = webdriver.Chrome()
#
# def randomchoice():                                                                  # 随机生成数字用于随机选中下拉框内容
#     temp = random.uniform(0,4)
#     return temp
#
# def sendresultemail(body,current_time):                 # 整合了发送邮件
#     sender = 'eugene.yue@gllue.com'                                                  # 发送邮箱
#     receiver = 'eugeneyueyujiang@163.com'                                            # 接收邮箱
#     subject = '申请试用-自动化提交结果截图'                                              # 发送邮件主题
#
#     username = 'eugene.yue@gllue.com'                                                # 发送邮箱用户/密码
#     password = 'Yyj19941224?'
#
#     msg = MIMEMultipart()                                                            # 构造一个MIMEMultipart对象代表邮件本身
#     msg['From'] = sender
#     msg['To'] = receiver
#     msg['Subject'] = subject
#
#     msg.attach(MIMEText(body, 'html', 'utf-8'))
#
#     pngname = current_time + '.png'                                                        # 确认截图文件名称
#
#     pngpath = '//Users/eugene/desktop/autoscreenshot/' + pngname                           # 根据文件名定位（本地）
#     pngpath = '//Users/eugene/Autotest/20181120/Autoscreenshot/' + pngname                 # 根据文件名定位（代码文件中）
#
#     with open(pngpath, 'r') as f:
#         mime = MIMEBase('image', 'png', filename = pngname)                                 # MIMEBase表示附件的对象
#         mime.add_header('Content-Disposition', 'attachment', filename = pngname)            # filename是显示附件名字
#         mime.add_header('Content-ID', '<0>')
#         mime.add_header('X-Attachment-Id', '0')
#         mime.set_payload(f.read())                                                          # 获取附件内容
#         encoders.encode_base64(mime)
#         msg.attach(mime)                                                                    # 作为附件添加到邮件
#
#     try:
#         smtp = smtplib.SMTP()                                                               # 邮件服务器
#         smtp.connect('smtphm.qiye.163.com')
#         smtp.login(username, password)
#         smtp.sendmail(sender, receiver, msg.as_string())
#         smtp.quit()
#     except smtplib.SMTPException as e:
#         tkinter.messagebox.showinfo("邮件发送失败", "Errorinfo: %s" % e)
#
# def shutchromedown(interval=3):
#     time.sleep(interval)                                                                    # 等待3秒
#     qd.quit()                                                                               # 关闭浏览器
#
# def testcase():
#     qd.get("http://www.gllue.com/home/product-hr")                                                  # 进入谷露申请试用界面
#     time.sleep(2)
#
#     # 定位申请试用按钮
#     # qd.find_element_by_xpath("/html/body/div/div/section/div/a[1]").click()                      # 通过xpath来定位申请试用按钮
#     qd.find_element_by_css_selector("body > div > div > section > div > a:nth-child(1)").click()   # 通过CSS来定位申请试用按钮
#     time.sleep(1)
#
#     # 自动填写表单
#     qd.find_element_by_id("company").send_keys("autotest")  # 定位输入框并输入关键字
#     qd.find_element_by_id("chineseName").send_keys("autotest")
#     qd.find_element_by_id("title").send_keys("autotest")
#     qd.find_element_by_id("location").send_keys("autotest")
#     qd.find_element_by_id("mobile").send_keys("18118393383")
#     qd.find_element_by_id("email").send_keys("eugene.yue@gllue.com")
#
#     # 关于选择下拉框
#     # qd.find_element_by_xpath("//*[@id='source']/option[3]").click()                               # 固定选择一个下拉值
#     tempchoice = int(randomchoice())
#     dropdownselection = qd.find_element_by_xpath("//*[@id='scale']")                                # 随机选择下拉框的value
#     Select(dropdownselection).select_by_index(tempchoice)
#
#     qd.find_element_by_id("message").send_keys("自动测试申请试用")
#
#     # qd.find_element_by_css_selector("#request > input.button").click()                             # 通过CSS定位申请试用按钮
#     # qd.find_element_by_xpath("//*[@id='request']/input[7]").click()                                # 通过xpath定位申请试用按钮
#
# def testemailcontent(start_time,duration):
#
#     content = """
#     <div><span style="font-size:18pt;"><strong>Test Report of Leads</strong></span></div>
#     <div>&nbsp;</div>
#     <div><strong>Start Time:&nbsp;</strong>""" + str(start_time) + """</div>
#     <div><strong>Duration:&nbsp;</strong>""" + str(duration) + """</div>
#     <div><strong>Status:&nbsp;</strong></div>
#     <div>&nbsp;</div>
#     <div>
#     <table border="1" cellpadding="1" cellspacing="1" style="width:500px;">
#     	<tbody align="center" valign="center">
#     		<tr>
#     			<td><strong>Test Group/Test Case</strong></td>
#     			<td><strong>Count</strong></td>
#     			<td><strong>Pass</strong></td>
#     			<td><strong>Fail</strong></td>
#     			<td><strong>Error</strong></td>
#     		</tr>
#     		<tr>
#     			<td>&nbsp;</td>
#     			<td>&nbsp;</td>
#     			<td>&nbsp;</td>
#     			<td>&nbsp;</td>
#     			<td>&nbsp;</td>
#     		</tr>
#     	</tbody>
#     </table>
#     <div>&nbsp;</div>
#     <div><em>Generate by auto-testing and please do not reply. -- Eugene</em></div>
#     </div>
#     """
#
#     return content
#
# # 点击提交之后自动截图
# time.sleep(1)
# current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
# qd.get_screenshot_as_file('//Users/eugene/desktop/autoscreenshot/' + current_time + '.png')            # 自动保存至桌面文件夹
# qd.get_screenshot_as_file('//Users/eugene/Autotest/20181120/Autoscreenshot/' + current_time + '.png')  # 自动保存至代码文件夹
#
# if __name__ == "__main__":
#     start_time = datetime.datetime.now()  # 记录开始时间
#
#     testcase()
#
#     end_time = datetime.datetime.now()  # 记录结束时间
#     testcaseduration = (end_time - start_time)
#
#     print("脚本运行时长：" + str(testcaseduration))
#
#     testemailcontent(start_time,testcaseduration)
#
#     sendresultemail(testemailcontent)
#
#     interval = 3
#     shutchromedown(interval)