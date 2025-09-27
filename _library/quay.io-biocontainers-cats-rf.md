---
layout: container
name:  "quay.io/biocontainers/cats-rf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cats-rf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cats-rf/container.yaml"
updated_at: "2025-09-27 03:10:02.207297"
latest: "1.0.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/cats-rf"
aliases:
 - "CATS_general_assembly_stats.R"
 - "CATS_rf"
 - "CATS_rf_add_uncovered_bases.R"
 - "CATS_rf_add_uncovered_transcripts.R"
 - "CATS_rf_compare"
 - "CATS_rf_comparison.Rmd"
 - "CATS_rf_cov_acc_analysis.R"
 - "CATS_rf_generate_assembly_score.R"
 - "CATS_rf_paired_end_read_analysis.R"
 - "CATS_rf_read_assignment_pe.R"
 - "CATS_rf_read_assignment_se.R"
 - "pysamstats"
 - "kallisto"
 - "ref-cache"
 - "bash"
 - "bashbug"
 - "cpuinfo"
 - "gawk-5.3.1"
 - "pandoc-lua"
 - "gawkbug"
 - "pandoc-server"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "h5tools_test_utils"
 - "basenc"
 - "b2sum"
 - "ls"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
 - "chown"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.0.1--hdfd78af_0"
 - "1.0.2--hdfd78af_0"
description: "singularity registry hpc automated addition for cats-rf"
config: {"url": "https://biocontainers.pro/tools/cats-rf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cats-rf", "latest": {"1.0.2--hdfd78af_0": "sha256:305ccb70aa188b0e53ea8565d97861c41ca8198a678e9adcf024b4eb83ccbc07"}, "tags": {"1.0.0--hdfd78af_0": "sha256:9f48c9e9ef9822c156d6cd7163808cfa60cc60f8e467aa4727695c61f5c979c5", "1.0.1--hdfd78af_0": "sha256:74016b5fc9057b5090430770c703bb10f32cdd6e1b53ec60e0387f79bf11de55", "1.0.2--hdfd78af_0": "sha256:305ccb70aa188b0e53ea8565d97861c41ca8198a678e9adcf024b4eb83ccbc07"}, "docker": "quay.io/biocontainers/cats-rf", "aliases": {"CATS_general_assembly_stats.R": "/usr/local/bin/CATS_general_assembly_stats.R", "CATS_rf": "/usr/local/bin/CATS_rf", "CATS_rf_add_uncovered_bases.R": "/usr/local/bin/CATS_rf_add_uncovered_bases.R", "CATS_rf_add_uncovered_transcripts.R": "/usr/local/bin/CATS_rf_add_uncovered_transcripts.R", "CATS_rf_compare": "/usr/local/bin/CATS_rf_compare", "CATS_rf_comparison.Rmd": "/usr/local/bin/CATS_rf_comparison.Rmd", "CATS_rf_cov_acc_analysis.R": "/usr/local/bin/CATS_rf_cov_acc_analysis.R", "CATS_rf_generate_assembly_score.R": "/usr/local/bin/CATS_rf_generate_assembly_score.R", "CATS_rf_paired_end_read_analysis.R": "/usr/local/bin/CATS_rf_paired_end_read_analysis.R", "CATS_rf_read_assignment_pe.R": "/usr/local/bin/CATS_rf_read_assignment_pe.R", "CATS_rf_read_assignment_se.R": "/usr/local/bin/CATS_rf_read_assignment_se.R", "pysamstats": "/usr/local/bin/pysamstats", "kallisto": "/usr/local/bin/kallisto", "ref-cache": "/usr/local/bin/ref-cache", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "cpuinfo": "/usr/local/bin/cpuinfo", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "pandoc-lua": "/usr/local/bin/pandoc-lua", "gawkbug": "/usr/local/bin/gawkbug", "pandoc-server": "/usr/local/bin/pandoc-server", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cats-rf.
singularity registry hpc automated addition for cats-rf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cats-rf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cats-rf:1.0.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cats-rf/1.0.2--hdfd78af_0
$ module help quay.io/biocontainers/cats-rf/1.0.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cats-rf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cats-rf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cats-rf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cats-rf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cats-rf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cats-rf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CATS_general_assembly_stats.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_general_assembly_stats.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_general_assembly_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_general_assembly_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_add_uncovered_bases.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_add_uncovered_bases.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_add_uncovered_bases.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_add_uncovered_bases.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_add_uncovered_transcripts.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_add_uncovered_transcripts.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_add_uncovered_transcripts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_add_uncovered_transcripts.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_compare

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_compare
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_comparison.Rmd

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_comparison.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_comparison.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_comparison.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_cov_acc_analysis.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_cov_acc_analysis.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_cov_acc_analysis.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_cov_acc_analysis.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_generate_assembly_score.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_generate_assembly_score.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_generate_assembly_score.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_generate_assembly_score.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_paired_end_read_analysis.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_paired_end_read_analysis.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_paired_end_read_analysis.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_paired_end_read_analysis.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_read_assignment_pe.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_read_assignment_pe.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_read_assignment_pe.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_read_assignment_pe.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rf_read_assignment_se.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_rf_read_assignment_se.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rf_read_assignment_se.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rf_read_assignment_se.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysamstats

```bash
$ singularity exec <container> /usr/local/bin/pysamstats
$ podman run --it --rm --entrypoint /usr/local/bin/pysamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ls

```bash
$ singularity exec <container> /usr/local/bin/ls
$ podman run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chcon

```bash
$ singularity exec <container> /usr/local/bin/chcon
$ podman run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chgrp

```bash
$ singularity exec <container> /usr/local/bin/chgrp
$ podman run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmod

```bash
$ singularity exec <container> /usr/local/bin/chmod
$ podman run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chown

```bash
$ singularity exec <container> /usr/local/bin/chown
$ podman run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
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