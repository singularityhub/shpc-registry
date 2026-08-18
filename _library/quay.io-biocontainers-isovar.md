---
layout: container
name:  "quay.io/biocontainers/isovar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isovar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isovar/container.yaml"
updated_at: "2026-08-18 03:40:19.674469"
latest: "1.7.1--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/isovar"
aliases:
 - "isovar"
 - "isovar-allele-counts"
 - "isovar-allele-reads"
 - "isovar-protein-sequences"
 - "isovar-reference-contexts"
 - "isovar-translations"
 - "isovar-variant-reads"
 - "isovar-variant-sequences"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "psl"
 - "psl-make-dafsa"
 - "pylint-config"
 - "varcode"
 - "varcode-genes"
 - "pyensembl"
 - "isort-identify-imports"
 - "pylint"
 - "pyreverse"
 - "symilar"
 - "isort"
 - "idna"
 - "get_gprof"
 - "protoc-gen-upb_minitable"
 - "h2benchmark"
 - "elastishadow"
 - "get_objgraph"
 - "undill"
 - "checksum-profile"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "elasticurl_cpp"
 - "elastipubsub"
versions:
 - "1.7.1--pyh106432d_0"
description: "singularity registry hpc automated addition for isovar"
config: {"url": "https://biocontainers.pro/tools/isovar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for isovar", "latest": {"1.7.1--pyh106432d_0": "sha256:5194195d39a6d46a21d221bc18510db42d5fc622c05d1993df8e3fab36ca0a9b"}, "tags": {"1.7.1--pyh106432d_0": "sha256:5194195d39a6d46a21d221bc18510db42d5fc622c05d1993df8e3fab36ca0a9b"}, "docker": "quay.io/biocontainers/isovar", "aliases": {"isovar": "/usr/local/bin/isovar", "isovar-allele-counts": "/usr/local/bin/isovar-allele-counts", "isovar-allele-reads": "/usr/local/bin/isovar-allele-reads", "isovar-protein-sequences": "/usr/local/bin/isovar-protein-sequences", "isovar-reference-contexts": "/usr/local/bin/isovar-reference-contexts", "isovar-translations": "/usr/local/bin/isovar-translations", "isovar-variant-reads": "/usr/local/bin/isovar-variant-reads", "isovar-variant-sequences": "/usr/local/bin/isovar-variant-sequences", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "psl": "/usr/local/bin/psl", "psl-make-dafsa": "/usr/local/bin/psl-make-dafsa", "pylint-config": "/usr/local/bin/pylint-config", "varcode": "/usr/local/bin/varcode", "varcode-genes": "/usr/local/bin/varcode-genes", "pyensembl": "/usr/local/bin/pyensembl", "isort-identify-imports": "/usr/local/bin/isort-identify-imports", "pylint": "/usr/local/bin/pylint", "pyreverse": "/usr/local/bin/pyreverse", "symilar": "/usr/local/bin/symilar", "isort": "/usr/local/bin/isort", "idna": "/usr/local/bin/idna", "get_gprof": "/usr/local/bin/get_gprof", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "h2benchmark": "/usr/local/bin/h2benchmark", "elastishadow": "/usr/local/bin/elastishadow", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "checksum-profile": "/usr/local/bin/checksum-profile", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isovar.
singularity registry hpc automated addition for isovar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isovar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isovar:1.7.1--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isovar/1.7.1--pyh106432d_0
$ module help quay.io/biocontainers/isovar/1.7.1--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isovar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isovar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isovar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isovar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isovar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isovar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isovar

```bash
$ singularity exec <container> /usr/local/bin/isovar
$ podman run --it --rm --entrypoint /usr/local/bin/isovar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-allele-counts

```bash
$ singularity exec <container> /usr/local/bin/isovar-allele-counts
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-allele-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-allele-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-allele-reads

```bash
$ singularity exec <container> /usr/local/bin/isovar-allele-reads
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-allele-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-allele-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-protein-sequences

```bash
$ singularity exec <container> /usr/local/bin/isovar-protein-sequences
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-protein-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-protein-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-reference-contexts

```bash
$ singularity exec <container> /usr/local/bin/isovar-reference-contexts
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-reference-contexts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-reference-contexts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-translations

```bash
$ singularity exec <container> /usr/local/bin/isovar-translations
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-translations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-translations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-variant-reads

```bash
$ singularity exec <container> /usr/local/bin/isovar-variant-reads
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-variant-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-variant-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isovar-variant-sequences

```bash
$ singularity exec <container> /usr/local/bin/isovar-variant-sequences
$ podman run --it --rm --entrypoint /usr/local/bin/isovar-variant-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isovar-variant-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl

```bash
$ singularity exec <container> /usr/local/bin/psl
$ podman run --it --rm --entrypoint /usr/local/bin/psl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl-make-dafsa

```bash
$ singularity exec <container> /usr/local/bin/psl-make-dafsa
$ podman run --it --rm --entrypoint /usr/local/bin/psl-make-dafsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl-make-dafsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint-config

```bash
$ singularity exec <container> /usr/local/bin/pylint-config
$ podman run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varcode

```bash
$ singularity exec <container> /usr/local/bin/varcode
$ podman run --it --rm --entrypoint /usr/local/bin/varcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varcode-genes

```bash
$ singularity exec <container> /usr/local/bin/varcode-genes
$ podman run --it --rm --entrypoint /usr/local/bin/varcode-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varcode-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyensembl

```bash
$ singularity exec <container> /usr/local/bin/pyensembl
$ podman run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint

```bash
$ singularity exec <container> /usr/local/bin/pylint
$ podman run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyreverse

```bash
$ singularity exec <container> /usr/local/bin/pyreverse
$ podman run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### symilar

```bash
$ singularity exec <container> /usr/local/bin/symilar
$ podman run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort

```bash
$ singularity exec <container> /usr/local/bin/isort
$ podman run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### elastipubsub5

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub5
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_app

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_app
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
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