# Gateway Load Balancing Protocol (GLBP)

![Network Topology](./topology-glbp-gateway-load-balancing-protocol.jpg)

## Scenario:

As an employee for a top-secret Government organization you are responsible for their advanced network. Several employees need to have access to send data, no matter what happens to the network. To enhance the reliability of the network you decide to configure GLBP (Gateway Load Balancing Protocol), in addition you want to configure load-balancing to make optimal use of the resources you have. Get the job done and you can get back to sipping Martinis...shaken not stirred.

## Goal:

* All IP addresses have been preconfigured for you.
* OSPF has been configured between router Dalton, Moore and MoneyPenny.
* Router MoneyPenny has a loopback0 interface (IP address 5.5.5.5) which is advertised into OSPF. This can be used for testing your configuration.
* Router Connery and Brosnan have 'ip routing' disabled. Their default-gateway is set to 7.7.7.7.
* Change the mac-addresses on Router Dalton and Moore on their F0/0 interfaces:
  - Dalton: 0000.0000.0001
  - Moore: 0000.0000.0002
* Configure GLBP between router Dalton and Moore on their F0/0 interfaces, the virtual IP address should be 7.7.7.7. Use group number 7.
* Enable GLBP plaintext authentication. Use the password 'vault'.
* Change the GLBP load-balancing so packets are forwarded based on the host.
* Change the GLBP priority of Router Dalton to 120.
* Enable GLBP preempt on both Routers.
* Change the GLBP timers so hello packets are sent every 50 msec, the holddown timer should be 500 msec.
* Enable interface tracking on router Dalton for Serial 1/0, you need to check for the line-protocol.
* The starting weight for Router Dalton should be 120. When the loopback0 interface goes down it should decrement by 50.
* When the weight drops below 80 Router Dalton should no longer be the AVF (Active Virtual Gateway). The weight should be at least 90 before Router Dalton can become the AVF again.

## Additional Resources:

## IOS:

c3640-jk9o3s-mz.124-16.bin

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=n_l_Xa5IYHY
