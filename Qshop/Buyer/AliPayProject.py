from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA91XOUtAt6npBHAsZJbidDcBWVNGGsMN3IdoW2II23HUW+BjMSXv0LK17ZB5DgslIHDmz3+jbPVGHujJXiVoHdj6llmg3uUkOgI9QeK3pFdppLvQNv+av6JaL7wXS9bM7n0jJBqioivg5zKtcABr70cXCFD57z58U3MFVkxhxZuQx5MSpY/nJy0CTXc6g89XvZT7Vtgx0feHOwC/VBOenltVkSalcjofEjQJEQaK2yXR6EIiSSnDq8DUY3NjH6D/F5xdD1lFkc6OFZHnovi0UOaTW/63Uw5jNpa8QDCjZWj/2U5Oyw9NiWBn4EWxMk8g+D5yFVmbXwRfV9LoWekO3bQIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA91XOUtAt6npBHAsZJbidDcBWVNGGsMN3IdoW2II23HUW+BjMSXv0LK17ZB5DgslIHDmz3+jbPVGHujJXiVoHdj6llmg3uUkOgI9QeK3pFdppLvQNv+av6JaL7wXS9bM7n0jJBqioivg5zKtcABr70cXCFD57z58U3MFVkxhxZuQx5MSpY/nJy0CTXc6g89XvZT7Vtgx0feHOwC/VBOenltVkSalcjofEjQJEQaK2yXR6EIiSSnDq8DUY3NjH6D/F5xdD1lFkc6OFZHnovi0UOaTW/63Uw5jNpa8QDCjZWj/2U5Oyw9NiWBn4EWxMk8g+D5yFVmbXwRfV9LoWekO3bQIDAQABAoIBAQDuCEZorLGD1+SReJzbELEVauWq+3sE4xjkG1+hPrBNuuJAIp14mzKDTPJTiEywscYUY/QYqaFVggF90LUuGtbTlbcG6YW3a/fpAgQQIE8SGQDhjz8sUHc7AKfrgU9l5viacxIEtox+MiZuMvx3nYB8gjYmBXxidFc/nVEeH4gD2/VP328tcdntyGbgLoCXfq2SR3nczcUvYFNjEa/FNEeUmv3X1QMTFkmqNUyJzpYkdDnsas6esLG9IAK+DP+DVam+a3TZ65KQdhMzU9vcQqJNYxSe5juT8UUJyE/sYfgt9oTIiQ2NGXZTBQu8t8+6vH0+izjPkgIeswXZopsG8Z6BAoGBAP0FT+qUPw4a8cpDKhggOQjqdbOxBz118Pd4apuQMw9T2DCTecBaBX3NfaSkUdCSpd16UBGY8HCLSUyqGfENXRxuEseDHmo4yytx+bVsZj6Df0dbIPjT119zod+C+t69ELJaMBCB2zIbDNUo8Oy4vWs9MByAGvFe2kRu+/FQjnvXAoGBAPo/WwhF60eTExXUjIC/36PH2darf/JVlrDSNJZ9QuUd1P5A0ydoOrlNnVbA7H/rLEOdNxgZSArEs/LIDCE2PL94q/T2+vJz9W4rwCvZxUg0HJdMQB7Zn480uZH+hYB1grRTu1hk4S9olL1VDMsQX+383Gdt9M5q21uzCadEaZ5bAoGAEcJlsZlmM59AiWndcoQQfMe4KzypvW6h0zzofrLIYrMH4aD4Ur/+0q2xu/SsqW8hpUIIjLOnbL7aDj+CQqElf/FZ8BcL83i5CfueA1Xwd0LTlDaZQd3cqB59piqTYT70BRC/fukecY3kgLG292agJP7OebGkMnzt5Q/FL1LwLVECgYAYwTmtGNWMcAUcTLlVZyWlWvi2nqJ6g3LzrOec12lNpuTR/fGlXU8p036z/UOn58iqK5wumxmgTxMJ+jYQ9v+NZU+FXQU4BLaLnnJVJCa63MTTRqy1IIwDK5EL2ySzr2wtkHbg6KHKActs60Pntof2z+Oxq5Pi83kdmhljXYYhLwKBgEuzv+YSThs1gHkHPofrFIRkBzWir2qMFFLmgz1NtaBUXaLyPQ4+J90r5xaokHA86Yv6DNQecLaDAQ5oXvhgSsL8o5fpbAgvcZQRb3TPboHrdmjYci6VfZbk0qmOP6ogJxkRvWUJZ8OTdcC7nM0SRrkx0pUCPGt1izYQgvlDt7nS
-----END RSA PRIVATE KEY-----"""
#实例化支付
alipay = AliPay(
    appid = "2016092200574016",
    app_notify_url = None,
    app_private_key_string = alipay_private_key_string,
    alipay_public_key_string = alipay_public_key_string,
    sign_type = "RSA2"
)

#实例化订单
order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no = "1000000001", #订单号
    total_amount = str(100),#支付金额，是字符串
    subject = "生鲜交易", #支付主题
    return_url = None,
    notify_url = None
)#网页支付订单

#拼接收款地址 = 支付宝网关+订单返回参数
result = "https://openapi.alipaydev.com/gateway.do?"+order_string

print(result)