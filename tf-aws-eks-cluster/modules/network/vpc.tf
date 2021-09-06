resource aws_vpc cluster_vpc {
    cidr_block = ""
    enable_dns_hostnames = true
    enable_dns_support = true

    tags = {
        Name = format("%s-vpc", var.cluster_name)
    }
}