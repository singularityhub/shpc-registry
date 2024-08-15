---
layout: container
name:  "quay.io/biocontainers/annotsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/annotsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/annotsv/container.yaml"
updated_at: "2024-08-15 03:03:49.501853"
latest: "3.4.2--py312hdfd78af_0"
container_url: "https://biocontainers.pro/tools/annotsv"
aliases:
 - "AnnotSV"
 - "INSTALL_annotations.sh"
 - "variantconvert"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "unzip"
 - "f2py3.11"
 - "gff2gff.py"
 - "vcf_sample_filter.py"
 - "basenc"
 - "vcf_filter.py"
 - "vcf_melt"
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
versions:
 - "3.3.5--py311hdfd78af_0"
 - "3.3.6--py311hdfd78af_0"
 - "3.3.7--py312hdfd78af_0"
 - "3.3.8--py312hdfd78af_0"
 - "3.3.9--py312hdfd78af_0"
 - "3.4--py312hdfd78af_0"
 - "3.4--py312hdfd78af_1"
 - "3.4.2--py312hdfd78af_0"
description: "singularity registry hpc automated addition for annotsv"
config: {"url": "https://biocontainers.pro/tools/annotsv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for annotsv", "latest": {"3.4.2--py312hdfd78af_0": "sha256:09cc20a86b61fc44b7c1a5d90af8a88fb5e8cacbe56c9938301f2c5fc6ae71fb"}, "tags": {"3.3.5--py311hdfd78af_0": "sha256:d34b5d969b943711658982e75d8da2ed27ffab6f9fdf39a0320c705392164242", "3.3.6--py311hdfd78af_0": "sha256:da68ccb7db82c7e371f4d56bbd58eb7723325ed89b79b40d605f2dcfe8e2c6e5", "3.3.7--py312hdfd78af_0": "sha256:9a577b87641d9a08e1961995c33f53997f14b95ca99c60df20a21fd5d38d0d21", "3.3.8--py312hdfd78af_0": "sha256:16e6508ad1b12def96688471721490e9f88b7f98a39db9ec644f8f2d781c7d6e", "3.3.9--py312hdfd78af_0": "sha256:d92ac857ce5408e07b902fdc58efacbd8a2347fbc287fe0bd6877cb7f2f242e4", "3.4--py312hdfd78af_0": "sha256:d1cfa29ecad964e4e38ab61bf98dfcded535386a1d4c9212c6da5d5b90e7bb69", "3.4--py312hdfd78af_1": "sha256:bb12e2d920f7f6583b5db91d24cfe6ed6fb8bed7be11d87e5d0cec0e279ee2a4", "3.4.2--py312hdfd78af_0": "sha256:09cc20a86b61fc44b7c1a5d90af8a88fb5e8cacbe56c9938301f2c5fc6ae71fb"}, "docker": "quay.io/biocontainers/annotsv", "aliases": {"AnnotSV": "/usr/local/bin/AnnotSV", "INSTALL_annotations.sh": "/usr/local/bin/INSTALL_annotations.sh", "variantconvert": "/usr/local/bin/variantconvert", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "unzip": "/usr/local/bin/unzip", "f2py3.11": "/usr/local/bin/f2py3.11", "gff2gff.py": "/usr/local/bin/gff2gff.py", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "basenc": "/usr/local/bin/basenc", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum", "comm": "/usr/local/bin/comm", "cp": "/usr/local/bin/cp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/annotsv.
singularity registry hpc automated addition for annotsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/annotsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/annotsv:3.4.2--py312hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/annotsv/3.4.2--py312hdfd78af_0
$ module help quay.io/biocontainers/annotsv/3.4.2--py312hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### annotsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### annotsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### annotsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### annotsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### annotsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### annotsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AnnotSV

```bash
$ singularity exec <container> /usr/local/bin/AnnotSV
$ podman run --it --rm --entrypoint /usr/local/bin/AnnotSV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnnotSV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### INSTALL_annotations.sh

```bash
$ singularity exec <container> /usr/local/bin/INSTALL_annotations.sh
$ podman run --it --rm --entrypoint /usr/local/bin/INSTALL_annotations.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/INSTALL_annotations.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variantconvert

```bash
$ singularity exec <container> /usr/local/bin/variantconvert
$ podman run --it --rm --entrypoint /usr/local/bin/variantconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variantconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
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