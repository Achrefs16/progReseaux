from netmiko import ConnectHandler

router={
       "device_type":"cisco_ios",
       "host":"sandbox-iosxe-latest-1.cisco.com",
       "username":"admin",
       "password":"C1sco12345",
       "port":22,}


try:
    con=ConnectHandler(**router)

    foutput=con.send_command("show clock")
    print(foutput)

    soutput=con.send_command("sh ip int br")

    with open("interfaces.txt","w") as f:
        f.write(soutput)

    commands=["interface loopback0",
          "ip address 10.8.8.8 255.255.255.240"
          "no shutdow"]

    toutput=con.send_config_set(commands)
    print("L'interface loopback a été configurée.")

except Exception as e:
    print(e)
