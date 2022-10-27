---
layout: container
name:  "quay.io/biocontainers/gnali"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gnali/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gnali/container.yaml"
updated_at: "2022-10-27 01:06:29.271135"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gnali"
aliases:
 - ".ensembl-vep-post-link.sh"
 - ".gnali-post-link.sh"
 - "bigWigToWig.pl"
 - "filter_vep"
 - "gnali"
 - "gnali_get_data"
 - "haplo"
 - "ibd2sdi"
 - "index_bigwigset.pl"
 - "mysql.server"
 - "mysql_config_editor"
 - "mysql_migrate_keyring"
 - "mysql_ssl_rsa_setup"
 - "mysqlpump"
 - "variant_recoder"
 - "vep"
 - "vep_convert_cache"
 - "vep_install"
 - "wigToBigWig.pl"
 - "zlib_decompress"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for gnali"
config: {"url": "https://biocontainers.pro/tools/gnali", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gnali", "latest": {"1.1.0--pyhdfd78af_0": "sha256:5a2fd37dcdea95218667fa41b240c64da76cbdbbd54f5912c584b9d8ce483de9"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:5a2fd37dcdea95218667fa41b240c64da76cbdbbd54f5912c584b9d8ce483de9"}, "docker": "quay.io/biocontainers/gnali", "aliases": {".ensembl-vep-post-link.sh": "/usr/local/bin/.ensembl-vep-post-link.sh", ".gnali-post-link.sh": "/usr/local/bin/.gnali-post-link.sh", "bigWigToWig.pl": "/usr/local/bin/bigWigToWig.pl", "filter_vep": "/usr/local/bin/filter_vep", "gnali": "/usr/local/bin/gnali", "gnali_get_data": "/usr/local/bin/gnali_get_data", "haplo": "/usr/local/bin/haplo", "ibd2sdi": "/usr/local/bin/ibd2sdi", "index_bigwigset.pl": "/usr/local/bin/index_bigwigset.pl", "mysql.server": "/usr/local/bin/mysql.server", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_migrate_keyring": "/usr/local/bin/mysql_migrate_keyring", "mysql_ssl_rsa_setup": "/usr/local/bin/mysql_ssl_rsa_setup", "mysqlpump": "/usr/local/bin/mysqlpump", "variant_recoder": "/usr/local/bin/variant_recoder", "vep": "/usr/local/bin/vep", "vep_convert_cache": "/usr/local/bin/vep_convert_cache", "vep_install": "/usr/local/bin/vep_install", "wigToBigWig.pl": "/usr/local/bin/wigToBigWig.pl", "zlib_decompress": "/usr/local/bin/zlib_decompress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gnali.
shpc-registry automated BioContainers addition for gnali
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gnali
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gnali:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gnali/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/gnali/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gnali-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gnali-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gnali-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gnali-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gnali-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gnali-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .ensembl-vep-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.ensembl-vep-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.ensembl-vep-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.ensembl-vep-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .gnali-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.gnali-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.gnali-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.gnali-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigToWig.pl

```bash
$ singularity exec <container> /usr/local/bin/bigWigToWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_vep

```bash
$ singularity exec <container> /usr/local/bin/filter_vep
$ podman run --it --rm --entrypoint /usr/local/bin/filter_vep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_vep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnali

```bash
$ singularity exec <container> /usr/local/bin/gnali
$ podman run --it --rm --entrypoint /usr/local/bin/gnali   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnali   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnali_get_data

```bash
$ singularity exec <container> /usr/local/bin/gnali_get_data
$ podman run --it --rm --entrypoint /usr/local/bin/gnali_get_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnali_get_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplo

```bash
$ singularity exec <container> /usr/local/bin/haplo
$ podman run --it --rm --entrypoint /usr/local/bin/haplo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibd2sdi

```bash
$ singularity exec <container> /usr/local/bin/ibd2sdi
$ podman run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_bigwigset.pl

```bash
$ singularity exec <container> /usr/local/bin/index_bigwigset.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql.server

```bash
$ singularity exec <container> /usr/local/bin/mysql.server
$ podman run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config_editor

```bash
$ singularity exec <container> /usr/local/bin/mysql_config_editor
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_migrate_keyring

```bash
$ singularity exec <container> /usr/local/bin/mysql_migrate_keyring
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_migrate_keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_migrate_keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_ssl_rsa_setup

```bash
$ singularity exec <container> /usr/local/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump

```bash
$ singularity exec <container> /usr/local/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variant_recoder

```bash
$ singularity exec <container> /usr/local/bin/variant_recoder
$ podman run --it --rm --entrypoint /usr/local/bin/variant_recoder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variant_recoder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep

```bash
$ singularity exec <container> /usr/local/bin/vep
$ podman run --it --rm --entrypoint /usr/local/bin/vep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_convert_cache

```bash
$ singularity exec <container> /usr/local/bin/vep_convert_cache
$ podman run --it --rm --entrypoint /usr/local/bin/vep_convert_cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_convert_cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_install

```bash
$ singularity exec <container> /usr/local/bin/vep_install
$ podman run --it --rm --entrypoint /usr/local/bin/vep_install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig.pl

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zlib_decompress

```bash
$ singularity exec <container> /usr/local/bin/zlib_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
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