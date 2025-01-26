library(bio3d)
traj <- read.dcd("nowatr.dcd")
pdb <- read.pdb("comp.pdb")
ca.inds <- atom.select(pdb, elety="CA")
xyz <- fit.xyz(fixed=pdb$xyz, mobile=traj, fixed.inds=ca.inds$xyz, mobile.inds=ca.inds$xyz)
dim(xyz) == dim(traj)
pc <- pca.xyz(xyz[,ca.inds$xyz])
png("pca.png")
par(
    cex.axis=1.1,   
    font.axis=2,    
    font.lab=2      
)
plot(pc,col=bwr.colors(nrow(xyz)))
dev.off()
hc <- hclust(dist(pc$z[,1:2]))
grps1 <- cutree(hc, k=4)
png("clust4.png")
par(
    cex.axis=1.1,   
    font.axis=2,    
    font.lab=2      
)
plot(pc, col=grps1)
dev.off()
grps2 <- cutree(hc, k=3)
png("clust3.png")
par(
    cex.axis=1.1,   
    font.axis=2,    
    font.lab=2      
)
plot(pc, col=grps2)
dev.off()
pc1 <- mktrj.pca(pc, pc=1, b=pc$au[,1], file="pc1.pdb")
pc2 <- mktrj.pca(pc, pc=2, b=pc$au[,2], file="pc2.pdb")
#write.ncdf(pc1, "trj_1.nc")
#write.ncdf(pc2, "trj_2.nc")
cij <- dccm(xyz[,ca.inds$xyz])
png("corr.png")
par(
    cex.axis=1.1,   
    font.axis=2,    
    font.lab=2      
)
plot(cij)
dev.off()
#pymol.dccm(cij,pdb,type="launch")

