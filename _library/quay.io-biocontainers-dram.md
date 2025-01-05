---
layout: container
name:  "quay.io/biocontainers/dram"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dram/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dram/container.yaml"
updated_at: "2025-01-05 03:44:02.627701"
latest: "1.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dram"
aliases:
 - "DRAM-setup.py"
 - "DRAM-v.py"
 - "DRAM.py"
 - "EukHighConfidenceFilter"
 - "covels-SE"
 - "coves-SE"
 - "eufindtRNA"
 - "fasta2gsi"
 - "sstofa"
 - "tRNAscan-SE"
 - "tRNAscan-SE.conf"
 - "trnascan-1.4"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
versions:
 - "1.3.5--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
 - "1.4.2--pyhdfd78af_0"
 - "1.4.5--pyhdfd78af_0"
 - "1.4.6--pyhdfd78af_0"
 - "1.4.6--pyhdfd78af_2"
 - "1.5.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for dram"
config: {"url": "https://biocontainers.pro/tools/dram", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dram", "latest": {"1.5.0--pyhdfd78af_0": "sha256:f6cf5a9b725cfe10beee5eda19d45efbe9ad8f44fc218feb97b80f75641d23f9"}, "tags": {"1.3.5--pyhdfd78af_0": "sha256:b5abb14e7b0ded7a36cbd2458c256bdf9344618fe7781d37222bb01fa36ba85e", "1.4.0--pyhdfd78af_0": "sha256:0ecc0fbc97a48bf66fb6b1f4d705373e66d3918f2e2cc073ec8295896a44c5bb", "1.4.2--pyhdfd78af_0": "sha256:3509d767454e0321542d3a09273a8f6751c28594845c99b573fdcd2939897fb3", "1.4.5--pyhdfd78af_0": "sha256:bee7c8c98893a8ab388ae32587b19326f108b16da8f907a63b9719417585d8ce", "1.4.6--pyhdfd78af_0": "sha256:d419657ae3805cf55c6bffef31abacebc08c826990275eb31a9bc536a35ae743", "1.4.6--pyhdfd78af_2": "sha256:820fef71c2d1b7b862a569a4dd6cf78518b7ac92ecf3ef86a09db3f5f1bd34e6", "1.5.0--pyhdfd78af_0": "sha256:f6cf5a9b725cfe10beee5eda19d45efbe9ad8f44fc218feb97b80f75641d23f9"}, "docker": "quay.io/biocontainers/dram", "aliases": {"DRAM-setup.py": "/usr/local/bin/DRAM-setup.py", "DRAM-v.py": "/usr/local/bin/DRAM-v.py", "DRAM.py": "/usr/local/bin/DRAM.py", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "eufindtRNA": "/usr/local/bin/eufindtRNA", "fasta2gsi": "/usr/local/bin/fasta2gsi", "sstofa": "/usr/local/bin/sstofa", "tRNAscan-SE": "/usr/local/bin/tRNAscan-SE", "tRNAscan-SE.conf": "/usr/local/bin/tRNAscan-SE.conf", "trnascan-1.4": "/usr/local/bin/trnascan-1.4", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dram.
shpc-registry automated BioContainers addition for dram
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dram
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dram:1.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dram/1.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/dram/1.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dram-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dram-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dram-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dram-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dram-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dram-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DRAM-setup.py

```bash
$ singularity exec <container> /usr/local/bin/DRAM-setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/DRAM-setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DRAM-setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DRAM-v.py

```bash
$ singularity exec <container> /usr/local/bin/DRAM-v.py
$ podman run --it --rm --entrypoint /usr/local/bin/DRAM-v.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DRAM-v.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DRAM.py

```bash
$ singularity exec <container> /usr/local/bin/DRAM.py
$ podman run --it --rm --entrypoint /usr/local/bin/DRAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DRAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covels-SE

```bash
$ singularity exec <container> /usr/local/bin/covels-SE
$ podman run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coves-SE

```bash
$ singularity exec <container> /usr/local/bin/coves-SE
$ podman run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eufindtRNA

```bash
$ singularity exec <container> /usr/local/bin/eufindtRNA
$ podman run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2gsi

```bash
$ singularity exec <container> /usr/local/bin/fasta2gsi
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sstofa

```bash
$ singularity exec <container> /usr/local/bin/sstofa
$ podman run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE.conf

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE.conf
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trnascan-1.4

```bash
$ singularity exec <container> /usr/local/bin/trnascan-1.4
$ podman run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
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