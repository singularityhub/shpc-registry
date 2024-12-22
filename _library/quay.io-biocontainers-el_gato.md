---
layout: container
name:  "quay.io/biocontainers/el_gato"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/el_gato/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/el_gato/container.yaml"
updated_at: "2024-12-22 03:20:34.146378"
latest: "1.20.1--py311h7e72e81_0"
container_url: "https://biocontainers.pro/tools/el_gato"
aliases:
 - "el_gato.py"
 - "elgato_report.py"
 - "gfPcr"
 - "isPcr"
 - "run_el_gato.nf"
 - "jwebserver"
 - "gfServer"
 - "nextflow.bak"
 - "nextflow"
 - "blastn_vdb"
 - "tblastn_vdb"
 - "test_pcre"
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
 - "chroot"
 - "cksum"
 - "comm"
 - "cp"
 - "csplit"
 - "cut"
 - "date"
versions:
 - "1.14.4--py311hdfd78af_0"
 - "1.15.2--py311hdfd78af_0"
 - "1.18.0--py311hdfd78af_0"
 - "1.19.0--py311hdfd78af_0"
 - "1.18.2--py311hdfd78af_0"
 - "1.20.1--py311h7e72e81_0"
description: "singularity registry hpc automated addition for el_gato"
config: {"url": "https://biocontainers.pro/tools/el_gato", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for el_gato", "latest": {"1.20.1--py311h7e72e81_0": "sha256:e39b7b10f24a2ea1ca86fb2f300575832f3c75e7c79c772268cfc6b72dc63100"}, "tags": {"1.14.4--py311hdfd78af_0": "sha256:d28834612de0e736a09a40324290e4152631ed22b4a2ef90e50867c6ee914be6", "1.15.2--py311hdfd78af_0": "sha256:343d3b3ba94540ab9482b9c58f7ac6a6162164245c79fceaf84219c2f6e82f1d", "1.18.0--py311hdfd78af_0": "sha256:0164abee1f22dd59bd2aa9b9c573162116b723eacc33db7ec9e41e3ed2b84997", "1.19.0--py311hdfd78af_0": "sha256:7ef1c6adc1781634e03134c47a4e19705e288f05fcabb6c726d6f31c034112bc", "1.18.2--py311hdfd78af_0": "sha256:6d94cb8840320f293ed7c0c4007cc319b0becf1b7be04a89f8bbce9a08dd0901", "1.20.1--py311h7e72e81_0": "sha256:e39b7b10f24a2ea1ca86fb2f300575832f3c75e7c79c772268cfc6b72dc63100"}, "docker": "quay.io/biocontainers/el_gato", "aliases": {"el_gato.py": "/usr/local/bin/el_gato.py", "elgato_report.py": "/usr/local/bin/elgato_report.py", "gfPcr": "/usr/local/bin/gfPcr", "isPcr": "/usr/local/bin/isPcr", "run_el_gato.nf": "/usr/local/bin/run_el_gato.nf", "jwebserver": "/usr/local/bin/jwebserver", "gfServer": "/usr/local/bin/gfServer", "nextflow.bak": "/usr/local/bin/nextflow.bak", "nextflow": "/usr/local/bin/nextflow", "blastn_vdb": "/usr/local/bin/blastn_vdb", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "test_pcre": "/usr/local/bin/test_pcre", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum", "comm": "/usr/local/bin/comm", "cp": "/usr/local/bin/cp", "csplit": "/usr/local/bin/csplit", "cut": "/usr/local/bin/cut", "date": "/usr/local/bin/date"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/el_gato.
singularity registry hpc automated addition for el_gato
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/el_gato
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/el_gato:1.20.1--py311h7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/el_gato/1.20.1--py311h7e72e81_0
$ module help quay.io/biocontainers/el_gato/1.20.1--py311h7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### el_gato-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### el_gato-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### el_gato-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### el_gato-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### el_gato-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### el_gato-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### el_gato.py

```bash
$ singularity exec <container> /usr/local/bin/el_gato.py
$ podman run --it --rm --entrypoint /usr/local/bin/el_gato.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/el_gato.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elgato_report.py

```bash
$ singularity exec <container> /usr/local/bin/elgato_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/elgato_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elgato_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfPcr

```bash
$ singularity exec <container> /usr/local/bin/gfPcr
$ podman run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isPcr

```bash
$ singularity exec <container> /usr/local/bin/isPcr
$ podman run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_el_gato.nf

```bash
$ singularity exec <container> /usr/local/bin/run_el_gato.nf
$ podman run --it --rm --entrypoint /usr/local/bin/run_el_gato.nf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_el_gato.nf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow

```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chroot

```bash
$ singularity exec <container> /usr/local/bin/chroot
$ podman run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cksum

```bash
$ singularity exec <container> /usr/local/bin/cksum
$ podman run --it --rm --entrypoint /usr/local/bin/cksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comm

```bash
$ singularity exec <container> /usr/local/bin/comm
$ podman run --it --rm --entrypoint /usr/local/bin/comm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp

```bash
$ singularity exec <container> /usr/local/bin/cp
$ podman run --it --rm --entrypoint /usr/local/bin/cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csplit

```bash
$ singularity exec <container> /usr/local/bin/csplit
$ podman run --it --rm --entrypoint /usr/local/bin/csplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut

```bash
$ singularity exec <container> /usr/local/bin/cut
$ podman run --it --rm --entrypoint /usr/local/bin/cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### date

```bash
$ singularity exec <container> /usr/local/bin/date
$ podman run --it --rm --entrypoint /usr/local/bin/date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/date   -v ${PWD} -w ${PWD} <container> -c " $@"
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