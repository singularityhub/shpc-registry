---
layout: container
name:  "quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19/container.yaml"
updated_at: "2023-04-02 19:06:16.482072"
latest: "3.00--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/ngsplotdb-ngsplotdb-hg19"
aliases:
 - "ExtractGName.R"
 - "alt_reg_cufflinks"
 - "alter2bed.pl"
 - "combine_diff.pl"
 - "coordinat.pl"
 - "difflist2bed.pl"
 - "get_difflist.pl"
 - "gtf2txt_plot.pl"
 - "install.db.tables.r"
 - "make_cgi_list.R"
 - "make_gene_model.R"
 - "ngs.plot.r"
 - "ngsplotdb.py"
 - "parse_diff.pl"
 - "plotCorrGram.r"
 - "remove.db.tables.r"
 - "replot.r"
 - "setTableDefaults.py"
 - "time.bigWig.extractOnly.r"
 - "time.bigWig.r"
 - "time.libload.r"
 - "time.ngs.plot.extractOnly.r"
 - "time.ngs.plot.r"
 - "time.tabix.2.r"
 - "time.tabix.extractOnly.r"
 - "time.tabix.r"
 - "wget"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "3.00--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for ngsplotdb-ngsplotdb-hg19"
config: {"url": "https://biocontainers.pro/tools/ngsplotdb-ngsplotdb-hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngsplotdb-ngsplotdb-hg19", "latest": {"3.00--r3.4.1_0": "sha256:f18d0e5ae45b8891217f8e479a85de8e98c530b9ac776d7620f589c6289e1637"}, "tags": {"3.00--r3.4.1_0": "sha256:f18d0e5ae45b8891217f8e479a85de8e98c530b9ac776d7620f589c6289e1637"}, "docker": "quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19", "aliases": {"ExtractGName.R": "/usr/local/bin/ExtractGName.R", "alt_reg_cufflinks": "/usr/local/bin/alt_reg_cufflinks", "alter2bed.pl": "/usr/local/bin/alter2bed.pl", "combine_diff.pl": "/usr/local/bin/combine_diff.pl", "coordinat.pl": "/usr/local/bin/coordinat.pl", "difflist2bed.pl": "/usr/local/bin/difflist2bed.pl", "get_difflist.pl": "/usr/local/bin/get_difflist.pl", "gtf2txt_plot.pl": "/usr/local/bin/gtf2txt_plot.pl", "install.db.tables.r": "/usr/local/bin/install.db.tables.r", "make_cgi_list.R": "/usr/local/bin/make_cgi_list.R", "make_gene_model.R": "/usr/local/bin/make_gene_model.R", "ngs.plot.r": "/usr/local/bin/ngs.plot.r", "ngsplotdb.py": "/usr/local/bin/ngsplotdb.py", "parse_diff.pl": "/usr/local/bin/parse_diff.pl", "plotCorrGram.r": "/usr/local/bin/plotCorrGram.r", "remove.db.tables.r": "/usr/local/bin/remove.db.tables.r", "replot.r": "/usr/local/bin/replot.r", "setTableDefaults.py": "/usr/local/bin/setTableDefaults.py", "time.bigWig.extractOnly.r": "/usr/local/bin/time.bigWig.extractOnly.r", "time.bigWig.r": "/usr/local/bin/time.bigWig.r", "time.libload.r": "/usr/local/bin/time.libload.r", "time.ngs.plot.extractOnly.r": "/usr/local/bin/time.ngs.plot.extractOnly.r", "time.ngs.plot.r": "/usr/local/bin/time.ngs.plot.r", "time.tabix.2.r": "/usr/local/bin/time.tabix.2.r", "time.tabix.extractOnly.r": "/usr/local/bin/time.tabix.extractOnly.r", "time.tabix.r": "/usr/local/bin/time.tabix.r", "wget": "/usr/local/bin/wget", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19.
shpc-registry automated BioContainers addition for ngsplotdb-ngsplotdb-hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19:3.00--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19/3.00--r3.4.1_0
$ module help quay.io/biocontainers/ngsplotdb-ngsplotdb-hg19/3.00--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngsplotdb-ngsplotdb-hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngsplotdb-ngsplotdb-hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngsplotdb-ngsplotdb-hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngsplotdb-ngsplotdb-hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngsplotdb-ngsplotdb-hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngsplotdb-ngsplotdb-hg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ExtractGName.R

```bash
$ singularity exec <container> /usr/local/bin/ExtractGName.R
$ podman run --it --rm --entrypoint /usr/local/bin/ExtractGName.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ExtractGName.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alt_reg_cufflinks

```bash
$ singularity exec <container> /usr/local/bin/alt_reg_cufflinks
$ podman run --it --rm --entrypoint /usr/local/bin/alt_reg_cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alt_reg_cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alter2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/alter2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alter2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alter2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_diff.pl

```bash
$ singularity exec <container> /usr/local/bin/combine_diff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combine_diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coordinat.pl

```bash
$ singularity exec <container> /usr/local/bin/coordinat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/coordinat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coordinat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### difflist2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/difflist2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/difflist2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/difflist2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_difflist.pl

```bash
$ singularity exec <container> /usr/local/bin/get_difflist.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_difflist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_difflist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2txt_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf2txt_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2txt_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2txt_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install.db.tables.r

```bash
$ singularity exec <container> /usr/local/bin/install.db.tables.r
$ podman run --it --rm --entrypoint /usr/local/bin/install.db.tables.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install.db.tables.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_cgi_list.R

```bash
$ singularity exec <container> /usr/local/bin/make_cgi_list.R
$ podman run --it --rm --entrypoint /usr/local/bin/make_cgi_list.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_cgi_list.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_gene_model.R

```bash
$ singularity exec <container> /usr/local/bin/make_gene_model.R
$ podman run --it --rm --entrypoint /usr/local/bin/make_gene_model.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_gene_model.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngs.plot.r

```bash
$ singularity exec <container> /usr/local/bin/ngs.plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/ngs.plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngs.plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngsplotdb.py

```bash
$ singularity exec <container> /usr/local/bin/ngsplotdb.py
$ podman run --it --rm --entrypoint /usr/local/bin/ngsplotdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsplotdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_diff.pl

```bash
$ singularity exec <container> /usr/local/bin/parse_diff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/parse_diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotCorrGram.r

```bash
$ singularity exec <container> /usr/local/bin/plotCorrGram.r
$ podman run --it --rm --entrypoint /usr/local/bin/plotCorrGram.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotCorrGram.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove.db.tables.r

```bash
$ singularity exec <container> /usr/local/bin/remove.db.tables.r
$ podman run --it --rm --entrypoint /usr/local/bin/remove.db.tables.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove.db.tables.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### replot.r

```bash
$ singularity exec <container> /usr/local/bin/replot.r
$ podman run --it --rm --entrypoint /usr/local/bin/replot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/replot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setTableDefaults.py

```bash
$ singularity exec <container> /usr/local/bin/setTableDefaults.py
$ podman run --it --rm --entrypoint /usr/local/bin/setTableDefaults.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setTableDefaults.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.bigWig.extractOnly.r

```bash
$ singularity exec <container> /usr/local/bin/time.bigWig.extractOnly.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.bigWig.extractOnly.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.bigWig.extractOnly.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.bigWig.r

```bash
$ singularity exec <container> /usr/local/bin/time.bigWig.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.bigWig.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.bigWig.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.libload.r

```bash
$ singularity exec <container> /usr/local/bin/time.libload.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.libload.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.libload.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.ngs.plot.extractOnly.r

```bash
$ singularity exec <container> /usr/local/bin/time.ngs.plot.extractOnly.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.ngs.plot.extractOnly.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.ngs.plot.extractOnly.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.ngs.plot.r

```bash
$ singularity exec <container> /usr/local/bin/time.ngs.plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.ngs.plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.ngs.plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.tabix.2.r

```bash
$ singularity exec <container> /usr/local/bin/time.tabix.2.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.tabix.2.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.tabix.2.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.tabix.extractOnly.r

```bash
$ singularity exec <container> /usr/local/bin/time.tabix.extractOnly.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.tabix.extractOnly.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.tabix.extractOnly.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time.tabix.r

```bash
$ singularity exec <container> /usr/local/bin/time.tabix.r
$ podman run --it --rm --entrypoint /usr/local/bin/time.tabix.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time.tabix.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)