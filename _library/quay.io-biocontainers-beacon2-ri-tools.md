---
layout: container
name:  "quay.io/biocontainers/beacon2-ri-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beacon2-ri-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/beacon2-ri-tools/container.yaml"
updated_at: "2024-11-08 03:00:45.374385"
latest: "2.0.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/beacon2-ri-tools"
aliases:
 - "beacon"
 - "bff-validator"
 - "bff2html.pl"
 - "bff2json.pl"
 - "crc32"
 - "csv2xlsx"
 - "extract_vba"
 - "hypnotoad"
 - "mojo"
 - "morbo"
 - "perl-doc"
 - "pxf2bff"
 - "vcf2bff.pl"
 - "yamlpp5-events"
 - "yamlpp5-highlight"
 - "yamlpp5-load"
 - "yamlpp5-load-dump"
 - "yamlpp5-parse-emit"
 - "pg_amcheck"
 - "pg_verifybackup"
 - "pg_checksums"
 - "tzselect"
 - "zdump"
 - "zic"
 - "oid2name"
 - "pg_receivewal"
 - "pg_resetwal"
 - "pg_waldump"
 - "vacuumlo"
 - "clusterdb"
 - "createdb"
 - "createuser"
 - "dropdb"
 - "dropuser"
 - "ecpg"
 - "initdb"
 - "pg_archivecleanup"
 - "pg_basebackup"
 - "pg_controldata"
 - "pg_ctl"
 - "pg_dump"
 - "pg_dumpall"
 - "pg_isready"
versions:
 - "2.0.0--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for beacon2-ri-tools"
config: {"url": "https://biocontainers.pro/tools/beacon2-ri-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for beacon2-ri-tools", "latest": {"2.0.0--pl5321hdfd78af_0": "sha256:ecad6829625c1f200412496557b1e2dabc963389478d6e7a543782d9fc230cac"}, "tags": {"2.0.0--pl5321hdfd78af_0": "sha256:ecad6829625c1f200412496557b1e2dabc963389478d6e7a543782d9fc230cac"}, "docker": "quay.io/biocontainers/beacon2-ri-tools", "aliases": {"beacon": "/usr/local/bin/beacon", "bff-validator": "/usr/local/bin/bff-validator", "bff2html.pl": "/usr/local/bin/bff2html.pl", "bff2json.pl": "/usr/local/bin/bff2json.pl", "crc32": "/usr/local/bin/crc32", "csv2xlsx": "/usr/local/bin/csv2xlsx", "extract_vba": "/usr/local/bin/extract_vba", "hypnotoad": "/usr/local/bin/hypnotoad", "mojo": "/usr/local/bin/mojo", "morbo": "/usr/local/bin/morbo", "perl-doc": "/usr/local/bin/perl-doc", "pxf2bff": "/usr/local/bin/pxf2bff", "vcf2bff.pl": "/usr/local/bin/vcf2bff.pl", "yamlpp5-events": "/usr/local/bin/yamlpp5-events", "yamlpp5-highlight": "/usr/local/bin/yamlpp5-highlight", "yamlpp5-load": "/usr/local/bin/yamlpp5-load", "yamlpp5-load-dump": "/usr/local/bin/yamlpp5-load-dump", "yamlpp5-parse-emit": "/usr/local/bin/yamlpp5-parse-emit", "pg_amcheck": "/usr/local/bin/pg_amcheck", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "pg_checksums": "/usr/local/bin/pg_checksums", "tzselect": "/usr/local/bin/tzselect", "zdump": "/usr/local/bin/zdump", "zic": "/usr/local/bin/zic", "oid2name": "/usr/local/bin/oid2name", "pg_receivewal": "/usr/local/bin/pg_receivewal", "pg_resetwal": "/usr/local/bin/pg_resetwal", "pg_waldump": "/usr/local/bin/pg_waldump", "vacuumlo": "/usr/local/bin/vacuumlo", "clusterdb": "/usr/local/bin/clusterdb", "createdb": "/usr/local/bin/createdb", "createuser": "/usr/local/bin/createuser", "dropdb": "/usr/local/bin/dropdb", "dropuser": "/usr/local/bin/dropuser", "ecpg": "/usr/local/bin/ecpg", "initdb": "/usr/local/bin/initdb", "pg_archivecleanup": "/usr/local/bin/pg_archivecleanup", "pg_basebackup": "/usr/local/bin/pg_basebackup", "pg_controldata": "/usr/local/bin/pg_controldata", "pg_ctl": "/usr/local/bin/pg_ctl", "pg_dump": "/usr/local/bin/pg_dump", "pg_dumpall": "/usr/local/bin/pg_dumpall", "pg_isready": "/usr/local/bin/pg_isready"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/beacon2-ri-tools.
singularity registry hpc automated addition for beacon2-ri-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beacon2-ri-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beacon2-ri-tools:2.0.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beacon2-ri-tools/2.0.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/beacon2-ri-tools/2.0.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beacon2-ri-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beacon2-ri-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beacon2-ri-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beacon2-ri-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beacon2-ri-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beacon2-ri-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beacon

```bash
$ singularity exec <container> /usr/local/bin/beacon
$ podman run --it --rm --entrypoint /usr/local/bin/beacon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beacon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bff-validator

```bash
$ singularity exec <container> /usr/local/bin/bff-validator
$ podman run --it --rm --entrypoint /usr/local/bin/bff-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bff-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bff2html.pl

```bash
$ singularity exec <container> /usr/local/bin/bff2html.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bff2html.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bff2html.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bff2json.pl

```bash
$ singularity exec <container> /usr/local/bin/bff2json.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bff2json.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bff2json.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xlsx

```bash
$ singularity exec <container> /usr/local/bin/csv2xlsx
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xlsx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xlsx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_vba

```bash
$ singularity exec <container> /usr/local/bin/extract_vba
$ podman run --it --rm --entrypoint /usr/local/bin/extract_vba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_vba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hypnotoad

```bash
$ singularity exec <container> /usr/local/bin/hypnotoad
$ podman run --it --rm --entrypoint /usr/local/bin/hypnotoad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypnotoad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mojo

```bash
$ singularity exec <container> /usr/local/bin/mojo
$ podman run --it --rm --entrypoint /usr/local/bin/mojo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mojo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### morbo

```bash
$ singularity exec <container> /usr/local/bin/morbo
$ podman run --it --rm --entrypoint /usr/local/bin/morbo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/morbo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl-doc

```bash
$ singularity exec <container> /usr/local/bin/perl-doc
$ podman run --it --rm --entrypoint /usr/local/bin/perl-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pxf2bff

```bash
$ singularity exec <container> /usr/local/bin/pxf2bff
$ podman run --it --rm --entrypoint /usr/local/bin/pxf2bff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pxf2bff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bff.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2bff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-events

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-events
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-highlight

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-highlight
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-highlight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-highlight   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-load

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-load
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-load-dump

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-load-dump
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-load-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-load-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-parse-emit

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-parse-emit
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-parse-emit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-parse-emit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_amcheck

```bash
$ singularity exec <container> /usr/local/bin/pg_amcheck
$ podman run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_verifybackup

```bash
$ singularity exec <container> /usr/local/bin/pg_verifybackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_checksums

```bash
$ singularity exec <container> /usr/local/bin/pg_checksums
$ podman run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tzselect

```bash
$ singularity exec <container> /usr/local/bin/tzselect
$ podman run --it --rm --entrypoint /usr/local/bin/tzselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tzselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdump

```bash
$ singularity exec <container> /usr/local/bin/zdump
$ podman run --it --rm --entrypoint /usr/local/bin/zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zic

```bash
$ singularity exec <container> /usr/local/bin/zic
$ podman run --it --rm --entrypoint /usr/local/bin/zic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oid2name

```bash
$ singularity exec <container> /usr/local/bin/oid2name
$ podman run --it --rm --entrypoint /usr/local/bin/oid2name   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oid2name   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_receivewal

```bash
$ singularity exec <container> /usr/local/bin/pg_receivewal
$ podman run --it --rm --entrypoint /usr/local/bin/pg_receivewal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_receivewal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_resetwal

```bash
$ singularity exec <container> /usr/local/bin/pg_resetwal
$ podman run --it --rm --entrypoint /usr/local/bin/pg_resetwal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_resetwal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_waldump

```bash
$ singularity exec <container> /usr/local/bin/pg_waldump
$ podman run --it --rm --entrypoint /usr/local/bin/pg_waldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_waldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vacuumlo

```bash
$ singularity exec <container> /usr/local/bin/vacuumlo
$ podman run --it --rm --entrypoint /usr/local/bin/vacuumlo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vacuumlo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterdb

```bash
$ singularity exec <container> /usr/local/bin/clusterdb
$ podman run --it --rm --entrypoint /usr/local/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createdb

```bash
$ singularity exec <container> /usr/local/bin/createdb
$ podman run --it --rm --entrypoint /usr/local/bin/createdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createuser

```bash
$ singularity exec <container> /usr/local/bin/createuser
$ podman run --it --rm --entrypoint /usr/local/bin/createuser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createuser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropdb

```bash
$ singularity exec <container> /usr/local/bin/dropdb
$ podman run --it --rm --entrypoint /usr/local/bin/dropdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropuser

```bash
$ singularity exec <container> /usr/local/bin/dropuser
$ podman run --it --rm --entrypoint /usr/local/bin/dropuser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropuser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecpg

```bash
$ singularity exec <container> /usr/local/bin/ecpg
$ podman run --it --rm --entrypoint /usr/local/bin/ecpg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecpg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### initdb

```bash
$ singularity exec <container> /usr/local/bin/initdb
$ podman run --it --rm --entrypoint /usr/local/bin/initdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/initdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_archivecleanup

```bash
$ singularity exec <container> /usr/local/bin/pg_archivecleanup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_archivecleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_archivecleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_basebackup

```bash
$ singularity exec <container> /usr/local/bin/pg_basebackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_basebackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_basebackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_controldata

```bash
$ singularity exec <container> /usr/local/bin/pg_controldata
$ podman run --it --rm --entrypoint /usr/local/bin/pg_controldata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_controldata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_ctl

```bash
$ singularity exec <container> /usr/local/bin/pg_ctl
$ podman run --it --rm --entrypoint /usr/local/bin/pg_ctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_ctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dump

```bash
$ singularity exec <container> /usr/local/bin/pg_dump
$ podman run --it --rm --entrypoint /usr/local/bin/pg_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dumpall

```bash
$ singularity exec <container> /usr/local/bin/pg_dumpall
$ podman run --it --rm --entrypoint /usr/local/bin/pg_dumpall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_dumpall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_isready

```bash
$ singularity exec <container> /usr/local/bin/pg_isready
$ podman run --it --rm --entrypoint /usr/local/bin/pg_isready   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_isready   -v ${PWD} -w ${PWD} <container> -c " $@"
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