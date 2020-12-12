# Plotting

### Boxplot using R

```text
## Add an alpha value to a colour
add.alpha <- function(col, alpha=1){
  if(missing(col))
    stop("Please provide a vector of colours.")
  apply(sapply(col, col2rgb)/255, 2, function(x) rgb(x[1], x[2], x[3], alpha=alpha))  
}

# data
x <- rep(1:10, each=7)
y <- rnorm(10*7)

# format for saving
png(file = "plotting.png", width = 600, height = 800)
# postscript("ft.eps", horizontal = FALSE, onefile = FALSE, family="Helvetica", bg="transparent", width = 8, height = 7)
par(col.axis="black", font.axis=3, cex.axis=1.8)

xticker <- c("Basic\n\n","New\n\n","Basic\n+\nDC",
             "Basic\n+\nRE","Basic\n+\nPSSP","Basic\n+\nRBP",
             "CbnF\n\n","CbnF\n+\nPSSP","CbnF\n+\nRBP",
             "     CbnF\n     +PSSP\n     +RBP  ")

c1 <-c("#FF1F00",  # 20 Scarlet
       "#FF5F00",  # 18 Tangelo
       "#FF9F00",  # 16 Gamboge
       "#FFDF00",  # 14 Gold
       "#DFFF00",  # 12 Apple green
       "#9FFF00",  # 10 Spring bud
       "#5FFF00",  #  8 Pistachio
       "#1FFF00",  #  6 Sap green
       "#1FFF00",  #  6 Sap green
       "#1FFF00",  #  6 Sap green
       "#00FF1F"   #  4 Emerald green
       )

c2 <- add.alpha(c1, alpha=0.3)
c3 <- c1


boxplot(y~x, 
    name = xticker,
    col=c2, 
    medcol=c3, 
    whiskcol=c1, 
    staplecol=c3,
    boxcol=c3, 
    # outcol=c3,
    # pch=23,
    # cex=2,
    xaxt = "n",
    # xlab= "Feature", 
    xlab = "",
    # ylab = expression(paste("MAE (", Phi, ")")),
    ylab = "",
    # cex.lab=1.5,
    axes=FALSE,
    font.axis=4,
    cex.axis=1.5,
    frame = FALSE
    )

title(ylab=expression(paste("MAE (", Phi, ")")), line=2.5, cex.lab=1.5)
stripchart(y~x, vertical = TRUE, method = "jitter", pch = 19, add = TRUE, col = c1)
# stripchart(y~x, vertical = TRUE, pch = 19, add = TRUE, col = c1)

# Add a legend
# legend("bottomleft", inset=.02, c("4","6","8"), fill=c2, horiz=TRUE, cex=0.8)
axis(1,seq(1, 10, by=1), labels=FALSE)
axis(2, font=1.75,las=2)
text(seq(1, 10, by=1), par("usr")[1] - 3, labels = xticker, 
    cex.axis=2.0, srt = 0, pos = 1, xpd = TRUE,
    cex = 1.35)

text(1, 2, "(a)", cex = 1.35)
```

