---
layout: container
name:  "quay.io/biocontainers/mobiorigin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mobiorigin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mobiorigin/container.yaml"
updated_at: "2026-10-10 19:15:38.240907"
latest: "0.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mobiorigin"
aliases:
 - "amrfinder_index"
 - "archive-peptide"
 - "cittest"
 - "combine-uids"
 - "compare-uids"
 - "disruption2genesymbol"
 - "exclude-uids"
 - "filter-records"
 - "gene2tbl"
 - "gpf2info"
 - "intersect-uids"
 - "mobiorigin"
 - "mutate"
 - "rcommon.sh"
 - "split-records"
 - "stx.prot"
 - "stxtyper"
 - "test-repeat"
 - "test_stxtyper.sh"
 - "uniq-count"
 - "uniq-count-rank"
 - "protoc-29.3.0"
 - "protoc-gen-upb-29.3.0"
 - "protoc-gen-upb_minitable-29.3.0"
 - "protoc-gen-upbdefs-29.3.0"
 - "amrfinder_update"
 - "dna_mutation"
 - "fasta2parts"
 - "amr_report"
 - "amrfinder"
 - "fasta_extract"
 - "gff_check"
 - "fasta_check"
 - "pyrodigal"
 - "archspec"
 - "archive-nlmnlp"
 - "archive-pids"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "pair-at-a-time"
versions:
 - "0.1.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mobiorigin"
config: {"url": "https://biocontainers.pro/tools/mobiorigin", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mobiorigin", "latest": {"0.1.5--pyhdfd78af_0": "sha256:ca23f56fcd64fbe321619d909b8a1699e82b779e2b65a6def6f4795fc3e1b268"}, "tags": {"0.1.5--pyhdfd78af_0": "sha256:ca23f56fcd64fbe321619d909b8a1699e82b779e2b65a6def6f4795fc3e1b268"}, "docker": "quay.io/biocontainers/mobiorigin", "aliases": {"amrfinder_index": "/usr/local/bin/amrfinder_index", "archive-peptide": "/usr/local/bin/archive-peptide", "cittest": "/usr/local/bin/cittest", "combine-uids": "/usr/local/bin/combine-uids", "compare-uids": "/usr/local/bin/compare-uids", "disruption2genesymbol": "/usr/local/bin/disruption2genesymbol", "exclude-uids": "/usr/local/bin/exclude-uids", "filter-records": "/usr/local/bin/filter-records", "gene2tbl": "/usr/local/bin/gene2tbl", "gpf2info": "/usr/local/bin/gpf2info", "intersect-uids": "/usr/local/bin/intersect-uids", "mobiorigin": "/usr/local/bin/mobiorigin", "mutate": "/usr/local/bin/mutate", "rcommon.sh": "/usr/local/bin/rcommon.sh", "split-records": "/usr/local/bin/split-records", "stx.prot": "/usr/local/bin/stx.prot", "stxtyper": "/usr/local/bin/stxtyper", "test-repeat": "/usr/local/bin/test-repeat", "test_stxtyper.sh": "/usr/local/bin/test_stxtyper.sh", "uniq-count": "/usr/local/bin/uniq-count", "uniq-count-rank": "/usr/local/bin/uniq-count-rank", "protoc-29.3.0": "/usr/local/bin/protoc-29.3.0", "protoc-gen-upb-29.3.0": "/usr/local/bin/protoc-gen-upb-29.3.0", "protoc-gen-upb_minitable-29.3.0": "/usr/local/bin/protoc-gen-upb_minitable-29.3.0", "protoc-gen-upbdefs-29.3.0": "/usr/local/bin/protoc-gen-upbdefs-29.3.0", "amrfinder_update": "/usr/local/bin/amrfinder_update", "dna_mutation": "/usr/local/bin/dna_mutation", "fasta2parts": "/usr/local/bin/fasta2parts", "amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "fasta_extract": "/usr/local/bin/fasta_extract", "gff_check": "/usr/local/bin/gff_check", "fasta_check": "/usr/local/bin/fasta_check", "pyrodigal": "/usr/local/bin/pyrodigal", "archspec": "/usr/local/bin/archspec", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mobiorigin.
singularity registry hpc automated addition for mobiorigin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mobiorigin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mobiorigin:0.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mobiorigin/0.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/mobiorigin/0.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mobiorigin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mobiorigin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mobiorigin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mobiorigin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mobiorigin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mobiorigin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amrfinder_index

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_index
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-peptide

```bash
$ singularity exec <container> /usr/local/bin/archive-peptide
$ podman run --it --rm --entrypoint /usr/local/bin/archive-peptide   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-peptide   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cittest

```bash
$ singularity exec <container> /usr/local/bin/cittest
$ podman run --it --rm --entrypoint /usr/local/bin/cittest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cittest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-uids

```bash
$ singularity exec <container> /usr/local/bin/combine-uids
$ podman run --it --rm --entrypoint /usr/local/bin/combine-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-uids

```bash
$ singularity exec <container> /usr/local/bin/compare-uids
$ podman run --it --rm --entrypoint /usr/local/bin/compare-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disruption2genesymbol

```bash
$ singularity exec <container> /usr/local/bin/disruption2genesymbol
$ podman run --it --rm --entrypoint /usr/local/bin/disruption2genesymbol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disruption2genesymbol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exclude-uids

```bash
$ singularity exec <container> /usr/local/bin/exclude-uids
$ podman run --it --rm --entrypoint /usr/local/bin/exclude-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exclude-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-records

```bash
$ singularity exec <container> /usr/local/bin/filter-records
$ podman run --it --rm --entrypoint /usr/local/bin/filter-records   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-records   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2tbl

```bash
$ singularity exec <container> /usr/local/bin/gene2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gene2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpf2info

```bash
$ singularity exec <container> /usr/local/bin/gpf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gpf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersect-uids

```bash
$ singularity exec <container> /usr/local/bin/intersect-uids
$ podman run --it --rm --entrypoint /usr/local/bin/intersect-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersect-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mobiorigin

```bash
$ singularity exec <container> /usr/local/bin/mobiorigin
$ podman run --it --rm --entrypoint /usr/local/bin/mobiorigin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mobiorigin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutate

```bash
$ singularity exec <container> /usr/local/bin/mutate
$ podman run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/rcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-records

```bash
$ singularity exec <container> /usr/local/bin/split-records
$ podman run --it --rm --entrypoint /usr/local/bin/split-records   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-records   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stx.prot

```bash
$ singularity exec <container> /usr/local/bin/stx.prot
$ podman run --it --rm --entrypoint /usr/local/bin/stx.prot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stx.prot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stxtyper

```bash
$ singularity exec <container> /usr/local/bin/stxtyper
$ podman run --it --rm --entrypoint /usr/local/bin/stxtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stxtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-repeat

```bash
$ singularity exec <container> /usr/local/bin/test-repeat
$ podman run --it --rm --entrypoint /usr/local/bin/test-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_stxtyper.sh

```bash
$ singularity exec <container> /usr/local/bin/test_stxtyper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/test_stxtyper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_stxtyper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-count

```bash
$ singularity exec <container> /usr/local/bin/uniq-count
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-count-rank

```bash
$ singularity exec <container> /usr/local/bin/uniq-count-rank
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-count-rank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-count-rank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder_update

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_update
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna_mutation

```bash
$ singularity exec <container> /usr/local/bin/dna_mutation
$ podman run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2parts

```bash
$ singularity exec <container> /usr/local/bin/fasta2parts
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amr_report

```bash
$ singularity exec <container> /usr/local/bin/amr_report
$ podman run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder

```bash
$ singularity exec <container> /usr/local/bin/amrfinder
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_extract

```bash
$ singularity exec <container> /usr/local/bin/fasta_extract
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_check

```bash
$ singularity exec <container> /usr/local/bin/gff_check
$ podman run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_check

```bash
$ singularity exec <container> /usr/local/bin/fasta_check
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
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