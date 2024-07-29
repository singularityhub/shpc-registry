---
layout: container
name:  "quay.io/biocontainers/circos-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/circos-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/circos-tools/container.yaml"
updated_at: "2024-07-29 17:29:56.037835"
latest: "0.23--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/circos-tools"
aliases:
 - "binlinks"
 - "bundlelinks"
 - "calcdatarange"
 - "clustal2link"
 - "colorinterpolate"
 - "convertlinks"
 - "filterlinks"
 - "make-conf"
 - "make-table"
 - "orderchr"
 - "parse-category"
 - "parse-table"
 - "randomdata"
 - "randomlinks"
 - "resample"
 - "config_data"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
 - "baseml"
 - "basemlg"
 - "chi2"
 - "codeml"
 - "evolver"
versions:
 - "0.23--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for circos-tools"
config: {"url": "https://biocontainers.pro/tools/circos-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for circos-tools", "latest": {"0.23--hdfd78af_3": "sha256:d3b4ceafff92761cd3a3fc5425c48bd6815fdb553fd795cb12fb84841d5b7fb9"}, "tags": {"0.23--hdfd78af_3": "sha256:d3b4ceafff92761cd3a3fc5425c48bd6815fdb553fd795cb12fb84841d5b7fb9"}, "docker": "quay.io/biocontainers/circos-tools", "aliases": {"binlinks": "/usr/local/bin/binlinks", "bundlelinks": "/usr/local/bin/bundlelinks", "calcdatarange": "/usr/local/bin/calcdatarange", "clustal2link": "/usr/local/bin/clustal2link", "colorinterpolate": "/usr/local/bin/colorinterpolate", "convertlinks": "/usr/local/bin/convertlinks", "filterlinks": "/usr/local/bin/filterlinks", "make-conf": "/usr/local/bin/make-conf", "make-table": "/usr/local/bin/make-table", "orderchr": "/usr/local/bin/orderchr", "parse-category": "/usr/local/bin/parse-category", "parse-table": "/usr/local/bin/parse-table", "randomdata": "/usr/local/bin/randomdata", "randomlinks": "/usr/local/bin/randomlinks", "resample": "/usr/local/bin/resample", "config_data": "/usr/local/bin/config_data", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "chi2": "/usr/local/bin/chi2", "codeml": "/usr/local/bin/codeml", "evolver": "/usr/local/bin/evolver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/circos-tools.
shpc-registry automated BioContainers addition for circos-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/circos-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/circos-tools:0.23--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/circos-tools/0.23--hdfd78af_3
$ module help quay.io/biocontainers/circos-tools/0.23--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circos-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circos-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circos-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circos-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circos-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circos-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binlinks

```bash
$ singularity exec <container> /usr/local/bin/binlinks
$ podman run --it --rm --entrypoint /usr/local/bin/binlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundlelinks

```bash
$ singularity exec <container> /usr/local/bin/bundlelinks
$ podman run --it --rm --entrypoint /usr/local/bin/bundlelinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundlelinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calcdatarange

```bash
$ singularity exec <container> /usr/local/bin/calcdatarange
$ podman run --it --rm --entrypoint /usr/local/bin/calcdatarange   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calcdatarange   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustal2link

```bash
$ singularity exec <container> /usr/local/bin/clustal2link
$ podman run --it --rm --entrypoint /usr/local/bin/clustal2link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustal2link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colorinterpolate

```bash
$ singularity exec <container> /usr/local/bin/colorinterpolate
$ podman run --it --rm --entrypoint /usr/local/bin/colorinterpolate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colorinterpolate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertlinks

```bash
$ singularity exec <container> /usr/local/bin/convertlinks
$ podman run --it --rm --entrypoint /usr/local/bin/convertlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterlinks

```bash
$ singularity exec <container> /usr/local/bin/filterlinks
$ podman run --it --rm --entrypoint /usr/local/bin/filterlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-conf

```bash
$ singularity exec <container> /usr/local/bin/make-conf
$ podman run --it --rm --entrypoint /usr/local/bin/make-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-table

```bash
$ singularity exec <container> /usr/local/bin/make-table
$ podman run --it --rm --entrypoint /usr/local/bin/make-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orderchr

```bash
$ singularity exec <container> /usr/local/bin/orderchr
$ podman run --it --rm --entrypoint /usr/local/bin/orderchr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orderchr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse-category

```bash
$ singularity exec <container> /usr/local/bin/parse-category
$ podman run --it --rm --entrypoint /usr/local/bin/parse-category   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse-category   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse-table

```bash
$ singularity exec <container> /usr/local/bin/parse-table
$ podman run --it --rm --entrypoint /usr/local/bin/parse-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randomdata

```bash
$ singularity exec <container> /usr/local/bin/randomdata
$ podman run --it --rm --entrypoint /usr/local/bin/randomdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randomdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randomlinks

```bash
$ singularity exec <container> /usr/local/bin/randomlinks
$ podman run --it --rm --entrypoint /usr/local/bin/randomlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randomlinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resample

```bash
$ singularity exec <container> /usr/local/bin/resample
$ podman run --it --rm --entrypoint /usr/local/bin/resample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chi2

```bash
$ singularity exec <container> /usr/local/bin/chi2
$ podman run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codeml

```bash
$ singularity exec <container> /usr/local/bin/codeml
$ podman run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evolver

```bash
$ singularity exec <container> /usr/local/bin/evolver
$ podman run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
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