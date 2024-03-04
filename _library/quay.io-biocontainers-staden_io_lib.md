---
layout: container
name:  "quay.io/biocontainers/staden_io_lib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staden_io_lib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/staden_io_lib/container.yaml"
updated_at: "2024-03-04 05:07:45.648818"
latest: "1.14.14--h0191234_7"
container_url: "https://biocontainers.pro/tools/staden_io_lib"
aliases:
 - "append_sff"
 - "convert_trace"
 - "cram_dump"
 - "cram_filter"
 - "cram_index"
 - "cram_size"
 - "extract_fastq"
 - "extract_qual"
 - "extract_seq"
 - "get_comment"
 - "hash_exp"
 - "hash_extract"
 - "hash_list"
 - "hash_sff"
 - "hash_tar"
 - "index_tar"
 - "io_lib-config"
 - "makeSCF"
 - "scf_dump"
 - "scf_info"
 - "scf_update"
 - "scram_flagstat"
 - "scram_merge"
 - "scram_pileup"
 - "scram_test"
 - "scramble"
 - "srf2fasta"
 - "srf2fastq"
 - "srf_dump_all"
 - "srf_extract_hash"
 - "srf_extract_linear"
 - "srf_filter"
 - "srf_index_hash"
 - "srf_info"
 - "srf_list"
 - "trace_dump"
 - "ztr_dump"
versions:
 - "1.14.14--h9ed8d9f_5"
 - "1.14.14--h9ed8d9f_6"
 - "1.14.14--h0191234_7"
description: "shpc-registry automated BioContainers addition for staden_io_lib"
config: {"url": "https://biocontainers.pro/tools/staden_io_lib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for staden_io_lib", "latest": {"1.14.14--h0191234_7": "sha256:deb68df505b8bcb70a04c2d8f107be279a6ba20dec6631d1596959d3b727cf4a"}, "tags": {"1.14.14--h9ed8d9f_5": "sha256:68bee137512586171be556687d66f42b8c53f7f9204d9448e9dadfdf57ec0b43", "1.14.14--h9ed8d9f_6": "sha256:e13d527dbc4a47ec0fc595b963c6a7d428eb670219caac74666567f6f6c20d82", "1.14.14--h0191234_7": "sha256:deb68df505b8bcb70a04c2d8f107be279a6ba20dec6631d1596959d3b727cf4a"}, "docker": "quay.io/biocontainers/staden_io_lib", "aliases": {"append_sff": "/usr/local/bin/append_sff", "convert_trace": "/usr/local/bin/convert_trace", "cram_dump": "/usr/local/bin/cram_dump", "cram_filter": "/usr/local/bin/cram_filter", "cram_index": "/usr/local/bin/cram_index", "cram_size": "/usr/local/bin/cram_size", "extract_fastq": "/usr/local/bin/extract_fastq", "extract_qual": "/usr/local/bin/extract_qual", "extract_seq": "/usr/local/bin/extract_seq", "get_comment": "/usr/local/bin/get_comment", "hash_exp": "/usr/local/bin/hash_exp", "hash_extract": "/usr/local/bin/hash_extract", "hash_list": "/usr/local/bin/hash_list", "hash_sff": "/usr/local/bin/hash_sff", "hash_tar": "/usr/local/bin/hash_tar", "index_tar": "/usr/local/bin/index_tar", "io_lib-config": "/usr/local/bin/io_lib-config", "makeSCF": "/usr/local/bin/makeSCF", "scf_dump": "/usr/local/bin/scf_dump", "scf_info": "/usr/local/bin/scf_info", "scf_update": "/usr/local/bin/scf_update", "scram_flagstat": "/usr/local/bin/scram_flagstat", "scram_merge": "/usr/local/bin/scram_merge", "scram_pileup": "/usr/local/bin/scram_pileup", "scram_test": "/usr/local/bin/scram_test", "scramble": "/usr/local/bin/scramble", "srf2fasta": "/usr/local/bin/srf2fasta", "srf2fastq": "/usr/local/bin/srf2fastq", "srf_dump_all": "/usr/local/bin/srf_dump_all", "srf_extract_hash": "/usr/local/bin/srf_extract_hash", "srf_extract_linear": "/usr/local/bin/srf_extract_linear", "srf_filter": "/usr/local/bin/srf_filter", "srf_index_hash": "/usr/local/bin/srf_index_hash", "srf_info": "/usr/local/bin/srf_info", "srf_list": "/usr/local/bin/srf_list", "trace_dump": "/usr/local/bin/trace_dump", "ztr_dump": "/usr/local/bin/ztr_dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/staden_io_lib.
shpc-registry automated BioContainers addition for staden_io_lib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staden_io_lib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staden_io_lib:1.14.14--h0191234_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staden_io_lib/1.14.14--h0191234_7
$ module help quay.io/biocontainers/staden_io_lib/1.14.14--h0191234_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staden_io_lib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staden_io_lib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staden_io_lib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staden_io_lib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staden_io_lib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staden_io_lib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### append_sff

```bash
$ singularity exec <container> /usr/local/bin/append_sff
$ podman run --it --rm --entrypoint /usr/local/bin/append_sff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/append_sff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_trace

```bash
$ singularity exec <container> /usr/local/bin/convert_trace
$ podman run --it --rm --entrypoint /usr/local/bin/convert_trace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_trace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cram_dump

```bash
$ singularity exec <container> /usr/local/bin/cram_dump
$ podman run --it --rm --entrypoint /usr/local/bin/cram_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cram_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cram_filter

```bash
$ singularity exec <container> /usr/local/bin/cram_filter
$ podman run --it --rm --entrypoint /usr/local/bin/cram_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cram_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cram_index

```bash
$ singularity exec <container> /usr/local/bin/cram_index
$ podman run --it --rm --entrypoint /usr/local/bin/cram_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cram_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cram_size

```bash
$ singularity exec <container> /usr/local/bin/cram_size
$ podman run --it --rm --entrypoint /usr/local/bin/cram_size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cram_size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fastq

```bash
$ singularity exec <container> /usr/local/bin/extract_fastq
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_qual

```bash
$ singularity exec <container> /usr/local/bin/extract_qual
$ podman run --it --rm --entrypoint /usr/local/bin/extract_qual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_qual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_seq

```bash
$ singularity exec <container> /usr/local/bin/extract_seq
$ podman run --it --rm --entrypoint /usr/local/bin/extract_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_comment

```bash
$ singularity exec <container> /usr/local/bin/get_comment
$ podman run --it --rm --entrypoint /usr/local/bin/get_comment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_comment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hash_exp

```bash
$ singularity exec <container> /usr/local/bin/hash_exp
$ podman run --it --rm --entrypoint /usr/local/bin/hash_exp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hash_exp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hash_extract

```bash
$ singularity exec <container> /usr/local/bin/hash_extract
$ podman run --it --rm --entrypoint /usr/local/bin/hash_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hash_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hash_list

```bash
$ singularity exec <container> /usr/local/bin/hash_list
$ podman run --it --rm --entrypoint /usr/local/bin/hash_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hash_list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hash_sff

```bash
$ singularity exec <container> /usr/local/bin/hash_sff
$ podman run --it --rm --entrypoint /usr/local/bin/hash_sff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hash_sff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hash_tar

```bash
$ singularity exec <container> /usr/local/bin/hash_tar
$ podman run --it --rm --entrypoint /usr/local/bin/hash_tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hash_tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_tar

```bash
$ singularity exec <container> /usr/local/bin/index_tar
$ podman run --it --rm --entrypoint /usr/local/bin/index_tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io_lib-config

```bash
$ singularity exec <container> /usr/local/bin/io_lib-config
$ podman run --it --rm --entrypoint /usr/local/bin/io_lib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_lib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeSCF

```bash
$ singularity exec <container> /usr/local/bin/makeSCF
$ podman run --it --rm --entrypoint /usr/local/bin/makeSCF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeSCF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scf_dump

```bash
$ singularity exec <container> /usr/local/bin/scf_dump
$ podman run --it --rm --entrypoint /usr/local/bin/scf_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scf_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scf_info

```bash
$ singularity exec <container> /usr/local/bin/scf_info
$ podman run --it --rm --entrypoint /usr/local/bin/scf_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scf_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scf_update

```bash
$ singularity exec <container> /usr/local/bin/scf_update
$ podman run --it --rm --entrypoint /usr/local/bin/scf_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scf_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scram_flagstat

```bash
$ singularity exec <container> /usr/local/bin/scram_flagstat
$ podman run --it --rm --entrypoint /usr/local/bin/scram_flagstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scram_flagstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scram_merge

```bash
$ singularity exec <container> /usr/local/bin/scram_merge
$ podman run --it --rm --entrypoint /usr/local/bin/scram_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scram_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scram_pileup

```bash
$ singularity exec <container> /usr/local/bin/scram_pileup
$ podman run --it --rm --entrypoint /usr/local/bin/scram_pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scram_pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scram_test

```bash
$ singularity exec <container> /usr/local/bin/scram_test
$ podman run --it --rm --entrypoint /usr/local/bin/scram_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scram_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scramble

```bash
$ singularity exec <container> /usr/local/bin/scramble
$ podman run --it --rm --entrypoint /usr/local/bin/scramble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scramble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf2fasta

```bash
$ singularity exec <container> /usr/local/bin/srf2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/srf2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf2fastq

```bash
$ singularity exec <container> /usr/local/bin/srf2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/srf2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_dump_all

```bash
$ singularity exec <container> /usr/local/bin/srf_dump_all
$ podman run --it --rm --entrypoint /usr/local/bin/srf_dump_all   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_dump_all   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_extract_hash

```bash
$ singularity exec <container> /usr/local/bin/srf_extract_hash
$ podman run --it --rm --entrypoint /usr/local/bin/srf_extract_hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_extract_hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_extract_linear

```bash
$ singularity exec <container> /usr/local/bin/srf_extract_linear
$ podman run --it --rm --entrypoint /usr/local/bin/srf_extract_linear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_extract_linear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_filter

```bash
$ singularity exec <container> /usr/local/bin/srf_filter
$ podman run --it --rm --entrypoint /usr/local/bin/srf_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_index_hash

```bash
$ singularity exec <container> /usr/local/bin/srf_index_hash
$ podman run --it --rm --entrypoint /usr/local/bin/srf_index_hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_index_hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_info

```bash
$ singularity exec <container> /usr/local/bin/srf_info
$ podman run --it --rm --entrypoint /usr/local/bin/srf_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srf_list

```bash
$ singularity exec <container> /usr/local/bin/srf_list
$ podman run --it --rm --entrypoint /usr/local/bin/srf_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srf_list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trace_dump

```bash
$ singularity exec <container> /usr/local/bin/trace_dump
$ podman run --it --rm --entrypoint /usr/local/bin/trace_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trace_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ztr_dump

```bash
$ singularity exec <container> /usr/local/bin/ztr_dump
$ podman run --it --rm --entrypoint /usr/local/bin/ztr_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ztr_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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