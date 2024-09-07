---
layout: container
name:  "quay.io/biocontainers/igdiscover"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/igdiscover/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/igdiscover/container.yaml"
updated_at: "2024-09-07 03:26:33.018178"
latest: "0.15.1--pyhdfd78af_2"
container_url: "https://biocontainers.pro/tools/igdiscover"
aliases:
 - "aclocal.bak"
 - "autoheader.bak"
 - "autom4te.bak"
 - "automake.bak"
 - "autoreconf.bak"
 - "autoscan.bak"
 - "autoupdate.bak"
 - "edit_imgt_file.pl"
 - "ifnames.bak"
 - "igblastn"
 - "igblastp"
 - "igdiscover"
 - "pear"
 - "pearRM"
 - "sqt"
 - "pyrsa-decrypt-bigfile"
 - "pyrsa-encrypt-bigfile"
 - "flash"
 - "cutadapt"
 - "vsearch"
 - "muscle"
 - "perl5.22.0"
 - "snakemake"
 - "snakemake-bash-completion"
 - "jp.py"
versions:
 - "0.9--py36_1"
 - "0.15.1--pyhdfd78af_0"
 - "0.14--pyhdfd78af_0"
 - "0.13--pyhdfd78af_0"
 - "0.12.3--py_1"
 - "0.11--py36_0"
 - "0.15.1--pyhdfd78af_1"
 - "0.15.1--pyhdfd78af_2"
description: "shpc-registry automated BioContainers addition for igdiscover"
config: {"url": "https://biocontainers.pro/tools/igdiscover", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for igdiscover", "latest": {"0.15.1--pyhdfd78af_2": "sha256:18d558a7afbfeb5736f2b23fcf8b9564edcfa2d65e50d2642ee85879aa26114c"}, "tags": {"0.9--py36_1": "sha256:4759f22626ddc66711108fa64aeed2b43e5b4fb91f3c08056fb27d33eb841b8e", "0.15.1--pyhdfd78af_0": "sha256:f3ce56d6828b2cf7898a7e7daecd3d83729f0b9ae5d2c8c0be188f87ab0ead28", "0.14--pyhdfd78af_0": "sha256:cc438b67c7aa540405aed692015e0a53872d76449020ad28f1ba968582fbe783", "0.13--pyhdfd78af_0": "sha256:03b8432cb55646cc2d5662f1fdb2328a3774ce469070b11eb9a66009a8d37744", "0.12.3--py_1": "sha256:80f6bfda27374457995f8c76f711530dfa544b27ea56607ad1792af89291a72b", "0.11--py36_0": "sha256:6949dec703acaea61ec72f190336aeb1acac7fa0d08448fab90bcbfa233795f6", "0.15.1--pyhdfd78af_1": "sha256:bf6d38be9b2154d669262d9582bcdcb9a5cf55c0d3f6fd67865bfba46a515d99", "0.15.1--pyhdfd78af_2": "sha256:18d558a7afbfeb5736f2b23fcf8b9564edcfa2d65e50d2642ee85879aa26114c"}, "docker": "quay.io/biocontainers/igdiscover", "aliases": {"aclocal.bak": "/usr/local/bin/aclocal.bak", "autoheader.bak": "/usr/local/bin/autoheader.bak", "autom4te.bak": "/usr/local/bin/autom4te.bak", "automake.bak": "/usr/local/bin/automake.bak", "autoreconf.bak": "/usr/local/bin/autoreconf.bak", "autoscan.bak": "/usr/local/bin/autoscan.bak", "autoupdate.bak": "/usr/local/bin/autoupdate.bak", "edit_imgt_file.pl": "/usr/local/bin/edit_imgt_file.pl", "ifnames.bak": "/usr/local/bin/ifnames.bak", "igblastn": "/usr/local/bin/igblastn", "igblastp": "/usr/local/bin/igblastp", "igdiscover": "/usr/local/bin/igdiscover", "pear": "/usr/local/bin/pear", "pearRM": "/usr/local/bin/pearRM", "sqt": "/usr/local/bin/sqt", "pyrsa-decrypt-bigfile": "/usr/local/bin/pyrsa-decrypt-bigfile", "pyrsa-encrypt-bigfile": "/usr/local/bin/pyrsa-encrypt-bigfile", "flash": "/usr/local/bin/flash", "cutadapt": "/usr/local/bin/cutadapt", "vsearch": "/usr/local/bin/vsearch", "muscle": "/usr/local/bin/muscle", "perl5.22.0": "/usr/local/bin/perl5.22.0", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "jp.py": "/usr/local/bin/jp.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/igdiscover.
shpc-registry automated BioContainers addition for igdiscover
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/igdiscover
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/igdiscover:0.15.1--pyhdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/igdiscover/0.15.1--pyhdfd78af_2
$ module help quay.io/biocontainers/igdiscover/0.15.1--pyhdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igdiscover-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igdiscover-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igdiscover-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igdiscover-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igdiscover-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igdiscover-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aclocal.bak

```bash
$ singularity exec <container> /usr/local/bin/aclocal.bak
$ podman run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoheader.bak

```bash
$ singularity exec <container> /usr/local/bin/autoheader.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autom4te.bak

```bash
$ singularity exec <container> /usr/local/bin/autom4te.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### automake.bak

```bash
$ singularity exec <container> /usr/local/bin/automake.bak
$ podman run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoreconf.bak

```bash
$ singularity exec <container> /usr/local/bin/autoreconf.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoscan.bak

```bash
$ singularity exec <container> /usr/local/bin/autoscan.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoupdate.bak

```bash
$ singularity exec <container> /usr/local/bin/autoupdate.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edit_imgt_file.pl

```bash
$ singularity exec <container> /usr/local/bin/edit_imgt_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/edit_imgt_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edit_imgt_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifnames.bak

```bash
$ singularity exec <container> /usr/local/bin/ifnames.bak
$ podman run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igblastn

```bash
$ singularity exec <container> /usr/local/bin/igblastn
$ podman run --it --rm --entrypoint /usr/local/bin/igblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igblastp

```bash
$ singularity exec <container> /usr/local/bin/igblastp
$ podman run --it --rm --entrypoint /usr/local/bin/igblastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igblastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igdiscover

```bash
$ singularity exec <container> /usr/local/bin/igdiscover
$ podman run --it --rm --entrypoint /usr/local/bin/igdiscover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igdiscover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pear

```bash
$ singularity exec <container> /usr/local/bin/pear
$ podman run --it --rm --entrypoint /usr/local/bin/pear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pearRM

```bash
$ singularity exec <container> /usr/local/bin/pearRM
$ podman run --it --rm --entrypoint /usr/local/bin/pearRM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pearRM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqt

```bash
$ singularity exec <container> /usr/local/bin/sqt
$ podman run --it --rm --entrypoint /usr/local/bin/sqt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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