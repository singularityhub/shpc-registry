---
layout: container
name:  "quay.io/biocontainers/magetab-curation-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magetab-curation-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/magetab-curation-scripts/container.yaml"
updated_at: "2025-05-02 03:54:18.944197"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/magetab-curation-scripts"
aliases:
 - "adf_checker.pl"
 - "check_atlas_eligibility.pl"
 - "comment_out_assays.pl"
 - "crc32"
 - "dm_date"
 - "dm_zdump"
 - "gal2adf.pl"
 - "launch_tracking_daemons.pl"
 - "magetab_insert_array.pl"
 - "magetab_insert_sub.pl"
 - "nimblegen2adf.pl"
 - "pg_verify_checksums"
 - "reset_array.pl"
 - "reset_experiment.pl"
 - "single_use_tracking_daemon.pl"
 - "split_magetab.pl"
 - "validate_magetab.pl"
 - "validjson"
 - "pod_cover"
 - "pg_standby"
 - "findrule"
 - "tzselect"
 - "zdump"
 - "zic"
 - "oid2name"
 - "pg_receivewal"
 - "pg_resetwal"
 - "pg_waldump"
versions:
 - "1.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for magetab-curation-scripts"
config: {"url": "https://biocontainers.pro/tools/magetab-curation-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for magetab-curation-scripts", "latest": {"1.1.0--hdfd78af_0": "sha256:9663f6919f09d859a0505e12aba3423febc38bb36bc19226e2359e7ab4b26868"}, "tags": {"1.1.0--hdfd78af_0": "sha256:9663f6919f09d859a0505e12aba3423febc38bb36bc19226e2359e7ab4b26868"}, "docker": "quay.io/biocontainers/magetab-curation-scripts", "aliases": {"adf_checker.pl": "/usr/local/bin/adf_checker.pl", "check_atlas_eligibility.pl": "/usr/local/bin/check_atlas_eligibility.pl", "comment_out_assays.pl": "/usr/local/bin/comment_out_assays.pl", "crc32": "/usr/local/bin/crc32", "dm_date": "/usr/local/bin/dm_date", "dm_zdump": "/usr/local/bin/dm_zdump", "gal2adf.pl": "/usr/local/bin/gal2adf.pl", "launch_tracking_daemons.pl": "/usr/local/bin/launch_tracking_daemons.pl", "magetab_insert_array.pl": "/usr/local/bin/magetab_insert_array.pl", "magetab_insert_sub.pl": "/usr/local/bin/magetab_insert_sub.pl", "nimblegen2adf.pl": "/usr/local/bin/nimblegen2adf.pl", "pg_verify_checksums": "/usr/local/bin/pg_verify_checksums", "reset_array.pl": "/usr/local/bin/reset_array.pl", "reset_experiment.pl": "/usr/local/bin/reset_experiment.pl", "single_use_tracking_daemon.pl": "/usr/local/bin/single_use_tracking_daemon.pl", "split_magetab.pl": "/usr/local/bin/split_magetab.pl", "validate_magetab.pl": "/usr/local/bin/validate_magetab.pl", "validjson": "/usr/local/bin/validjson", "pod_cover": "/usr/local/bin/pod_cover", "pg_standby": "/usr/local/bin/pg_standby", "findrule": "/usr/local/bin/findrule", "tzselect": "/usr/local/bin/tzselect", "zdump": "/usr/local/bin/zdump", "zic": "/usr/local/bin/zic", "oid2name": "/usr/local/bin/oid2name", "pg_receivewal": "/usr/local/bin/pg_receivewal", "pg_resetwal": "/usr/local/bin/pg_resetwal", "pg_waldump": "/usr/local/bin/pg_waldump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magetab-curation-scripts.
shpc-registry automated BioContainers addition for magetab-curation-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magetab-curation-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magetab-curation-scripts:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magetab-curation-scripts/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/magetab-curation-scripts/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magetab-curation-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magetab-curation-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magetab-curation-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magetab-curation-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magetab-curation-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magetab-curation-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adf_checker.pl

```bash
$ singularity exec <container> /usr/local/bin/adf_checker.pl
$ podman run --it --rm --entrypoint /usr/local/bin/adf_checker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adf_checker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_atlas_eligibility.pl

```bash
$ singularity exec <container> /usr/local/bin/check_atlas_eligibility.pl
$ podman run --it --rm --entrypoint /usr/local/bin/check_atlas_eligibility.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_atlas_eligibility.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comment_out_assays.pl

```bash
$ singularity exec <container> /usr/local/bin/comment_out_assays.pl
$ podman run --it --rm --entrypoint /usr/local/bin/comment_out_assays.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comment_out_assays.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_date

```bash
$ singularity exec <container> /usr/local/bin/dm_date
$ podman run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_zdump

```bash
$ singularity exec <container> /usr/local/bin/dm_zdump
$ podman run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gal2adf.pl

```bash
$ singularity exec <container> /usr/local/bin/gal2adf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gal2adf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gal2adf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### launch_tracking_daemons.pl

```bash
$ singularity exec <container> /usr/local/bin/launch_tracking_daemons.pl
$ podman run --it --rm --entrypoint /usr/local/bin/launch_tracking_daemons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/launch_tracking_daemons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magetab_insert_array.pl

```bash
$ singularity exec <container> /usr/local/bin/magetab_insert_array.pl
$ podman run --it --rm --entrypoint /usr/local/bin/magetab_insert_array.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magetab_insert_array.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magetab_insert_sub.pl

```bash
$ singularity exec <container> /usr/local/bin/magetab_insert_sub.pl
$ podman run --it --rm --entrypoint /usr/local/bin/magetab_insert_sub.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magetab_insert_sub.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nimblegen2adf.pl

```bash
$ singularity exec <container> /usr/local/bin/nimblegen2adf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nimblegen2adf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nimblegen2adf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_verify_checksums

```bash
$ singularity exec <container> /usr/local/bin/pg_verify_checksums
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verify_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verify_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reset_array.pl

```bash
$ singularity exec <container> /usr/local/bin/reset_array.pl
$ podman run --it --rm --entrypoint /usr/local/bin/reset_array.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reset_array.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reset_experiment.pl

```bash
$ singularity exec <container> /usr/local/bin/reset_experiment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/reset_experiment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reset_experiment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_use_tracking_daemon.pl

```bash
$ singularity exec <container> /usr/local/bin/single_use_tracking_daemon.pl
$ podman run --it --rm --entrypoint /usr/local/bin/single_use_tracking_daemon.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_use_tracking_daemon.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_magetab.pl

```bash
$ singularity exec <container> /usr/local/bin/split_magetab.pl
$ podman run --it --rm --entrypoint /usr/local/bin/split_magetab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_magetab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_magetab.pl

```bash
$ singularity exec <container> /usr/local/bin/validate_magetab.pl
$ podman run --it --rm --entrypoint /usr/local/bin/validate_magetab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_magetab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validjson

```bash
$ singularity exec <container> /usr/local/bin/validjson
$ podman run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod_cover

```bash
$ singularity exec <container> /usr/local/bin/pod_cover
$ podman run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_standby

```bash
$ singularity exec <container> /usr/local/bin/pg_standby
$ podman run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
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