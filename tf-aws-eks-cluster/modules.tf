module cluster {
    source = "./modules/cluster"
    cluster_name = var.cluster_name 
    aws_region = var.aws_region

    cluster_vpc   = module.network.cluster_vpc
    private_subnet_1a   = module.network.private_subnet_1a
    private_subnet_1c   = module.network.private_subnet_1c
}

module network {
    source = "./modules/network"
    cluster_name = var.cluster_name
    aws_region = var.aws_region
}