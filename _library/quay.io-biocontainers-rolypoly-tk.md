---
layout: container
name:  "quay.io/biocontainers/rolypoly-tk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rolypoly-tk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rolypoly-tk/container.yaml"
updated_at: "2026-08-03 06:37:18.496843"
latest: "0.7.17--pyh1f0d9b5_0"
container_url: "https://biocontainers.pro/tools/rolypoly-tk"
aliases:
 - "AUTHORS"
 - "bbmapy-ensure-java"
 - "bbmapy-test"
 - "draw_circular_plot"
 - "falco"
 - "gawk-5.4.1"
 - "generate-bbmapy-commands"
 - "gflags.py"
 - "gflags2man.py"
 - "linearfold"
 - "penguin"
 - "plass"
 - "pyrodigal-rv"
 - "rolypoly"
 - "testcons"
 - "binspreader"
 - "pathracer-seq-fs"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "spades-hpc"
 - "MitoHighConfidenceFilter"
 - "bwa-mem2"
 - "bwa-mem2.avx"
 - "bwa-mem2.avx2"
 - "bwa-mem2.avx512bw"
 - "bwa-mem2.sse41"
 - "bwa-mem2.sse42"
 - "pathracer"
 - "spades-gfa-split"
 - "RNAconsensus"
 - "EukHighConfidenceFilter"
 - "covels-SE"
 - "coves-SE"
 - "eufindtRNA"
 - "fasta2gsi"
 - "sstofa"
 - "tRNAscan-SE"
 - "tRNAscan-SE.conf"
versions:
 - "0.7.17--pyh1f0d9b5_0"
description: "singularity registry hpc automated addition for rolypoly-tk"
config: {"url": "https://biocontainers.pro/tools/rolypoly-tk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rolypoly-tk", "latest": {"0.7.17--pyh1f0d9b5_0": "sha256:e3206fbd732dc5b0cf736deccc20c0d8c13108c1697c69e94b45229bb7e3f9ed"}, "tags": {"0.7.17--pyh1f0d9b5_0": "sha256:e3206fbd732dc5b0cf736deccc20c0d8c13108c1697c69e94b45229bb7e3f9ed"}, "docker": "quay.io/biocontainers/rolypoly-tk", "aliases": {"AUTHORS": "/usr/local/bin/AUTHORS", "bbmapy-ensure-java": "/usr/local/bin/bbmapy-ensure-java", "bbmapy-test": "/usr/local/bin/bbmapy-test", "draw_circular_plot": "/usr/local/bin/draw_circular_plot", "falco": "/usr/local/bin/falco", "gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "generate-bbmapy-commands": "/usr/local/bin/generate-bbmapy-commands", "gflags.py": "/usr/local/bin/gflags.py", "gflags2man.py": "/usr/local/bin/gflags2man.py", "linearfold": "/usr/local/bin/linearfold", "penguin": "/usr/local/bin/penguin", "plass": "/usr/local/bin/plass", "pyrodigal-rv": "/usr/local/bin/pyrodigal-rv", "rolypoly": "/usr/local/bin/rolypoly", "testcons": "/usr/local/bin/testcons", "binspreader": "/usr/local/bin/binspreader", "pathracer-seq-fs": "/usr/local/bin/pathracer-seq-fs", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "spades-hpc": "/usr/local/bin/spades-hpc", "MitoHighConfidenceFilter": "/usr/local/bin/MitoHighConfidenceFilter", "bwa-mem2": "/usr/local/bin/bwa-mem2", "bwa-mem2.avx": "/usr/local/bin/bwa-mem2.avx", "bwa-mem2.avx2": "/usr/local/bin/bwa-mem2.avx2", "bwa-mem2.avx512bw": "/usr/local/bin/bwa-mem2.avx512bw", "bwa-mem2.sse41": "/usr/local/bin/bwa-mem2.sse41", "bwa-mem2.sse42": "/usr/local/bin/bwa-mem2.sse42", "pathracer": "/usr/local/bin/pathracer", "spades-gfa-split": "/usr/local/bin/spades-gfa-split", "RNAconsensus": "/usr/local/bin/RNAconsensus", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "eufindtRNA": "/usr/local/bin/eufindtRNA", "fasta2gsi": "/usr/local/bin/fasta2gsi", "sstofa": "/usr/local/bin/sstofa", "tRNAscan-SE": "/usr/local/bin/tRNAscan-SE", "tRNAscan-SE.conf": "/usr/local/bin/tRNAscan-SE.conf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rolypoly-tk.
singularity registry hpc automated addition for rolypoly-tk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rolypoly-tk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rolypoly-tk:0.7.17--pyh1f0d9b5_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rolypoly-tk/0.7.17--pyh1f0d9b5_0
$ module help quay.io/biocontainers/rolypoly-tk/0.7.17--pyh1f0d9b5_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rolypoly-tk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rolypoly-tk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rolypoly-tk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rolypoly-tk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rolypoly-tk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rolypoly-tk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AUTHORS

```bash
$ singularity exec <container> /usr/local/bin/AUTHORS
$ podman run --it --rm --entrypoint /usr/local/bin/AUTHORS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AUTHORS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbmapy-ensure-java

```bash
$ singularity exec <container> /usr/local/bin/bbmapy-ensure-java
$ podman run --it --rm --entrypoint /usr/local/bin/bbmapy-ensure-java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmapy-ensure-java   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbmapy-test

```bash
$ singularity exec <container> /usr/local/bin/bbmapy-test
$ podman run --it --rm --entrypoint /usr/local/bin/bbmapy-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmapy-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_circular_plot

```bash
$ singularity exec <container> /usr/local/bin/draw_circular_plot
$ podman run --it --rm --entrypoint /usr/local/bin/draw_circular_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_circular_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### falco

```bash
$ singularity exec <container> /usr/local/bin/falco
$ podman run --it --rm --entrypoint /usr/local/bin/falco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate-bbmapy-commands

```bash
$ singularity exec <container> /usr/local/bin/generate-bbmapy-commands
$ podman run --it --rm --entrypoint /usr/local/bin/generate-bbmapy-commands   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate-bbmapy-commands   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags.py

```bash
$ singularity exec <container> /usr/local/bin/gflags.py
$ podman run --it --rm --entrypoint /usr/local/bin/gflags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags2man.py

```bash
$ singularity exec <container> /usr/local/bin/gflags2man.py
$ podman run --it --rm --entrypoint /usr/local/bin/gflags2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linearfold

```bash
$ singularity exec <container> /usr/local/bin/linearfold
$ podman run --it --rm --entrypoint /usr/local/bin/linearfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linearfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### penguin

```bash
$ singularity exec <container> /usr/local/bin/penguin
$ podman run --it --rm --entrypoint /usr/local/bin/penguin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/penguin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plass

```bash
$ singularity exec <container> /usr/local/bin/plass
$ podman run --it --rm --entrypoint /usr/local/bin/plass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal-rv

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal-rv
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal-rv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal-rv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rolypoly

```bash
$ singularity exec <container> /usr/local/bin/rolypoly
$ podman run --it --rm --entrypoint /usr/local/bin/rolypoly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rolypoly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testcons

```bash
$ singularity exec <container> /usr/local/bin/testcons
$ podman run --it --rm --entrypoint /usr/local/bin/testcons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testcons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binspreader

```bash
$ singularity exec <container> /usr/local/bin/binspreader
$ podman run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer-seq-fs

```bash
$ singularity exec <container> /usr/local/bin/pathracer-seq-fs
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### spades-hpc

```bash
$ singularity exec <container> /usr/local/bin/spades-hpc
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MitoHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/MitoHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer

```bash
$ singularity exec <container> /usr/local/bin/pathracer
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gfa-split

```bash
$ singularity exec <container> /usr/local/bin/spades-gfa-split
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAconsensus

```bash
$ singularity exec <container> /usr/local/bin/RNAconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
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