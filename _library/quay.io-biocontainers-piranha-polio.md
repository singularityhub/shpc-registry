---
layout: container
name:  "quay.io/biocontainers/piranha-polio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piranha-polio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piranha-polio/container.yaml"
updated_at: "2023-04-07 02:42:22.993711"
latest: "1.0.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/piranha-polio"
aliases:
 - "check_compression"
 - "compress_fast5"
 - "consensus.smk"
 - "demux_fast5"
 - "fast5_subset"
 - "hdf2tf.py"
 - "import_pb_to_tensorboard"
 - "medaka"
 - "medaka_consensus"
 - "medaka_counts"
 - "medaka_data_path"
 - "medaka_haploid_variant"
 - "medaka_version_report"
 - "mini_align"
 - "multi_to_single_fast5"
 - "piranha"
 - "piranha_preprocessing.smk"
 - "piranha_vp1.smk"
 - "piranha_wg_2tile.smk"
 - "single_to_multi_fast5"
 - "snipit"
 - "snipit.smk"
 - "snp_functions.py"
 - "variation.smk"
 - "aec"
 - "plac_runner.py"
 - "yte"
 - "minimap2.py"
 - "estimator_ckpt_converter"
 - "mako-render"
 - "docutils"
 - "google-oauthlib-tool"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "tar"
 - "gff2gff.py"
 - "pulptest"
 - "tf_upgrade_v2"
 - "cbc"
 - "clp"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
 - "toco_from_protos"
versions:
 - "1.0.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for piranha-polio"
config: {"url": "https://biocontainers.pro/tools/piranha-polio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for piranha-polio", "latest": {"1.0.8--pyhdfd78af_0": "sha256:68ea13905d2776336c5cf59c1785a674dc6a87ff6468fddd7b258f088c1b4997"}, "tags": {"1.0.8--pyhdfd78af_0": "sha256:68ea13905d2776336c5cf59c1785a674dc6a87ff6468fddd7b258f088c1b4997"}, "docker": "quay.io/biocontainers/piranha-polio", "aliases": {"check_compression": "/usr/local/bin/check_compression", "compress_fast5": "/usr/local/bin/compress_fast5", "consensus.smk": "/usr/local/bin/consensus.smk", "demux_fast5": "/usr/local/bin/demux_fast5", "fast5_subset": "/usr/local/bin/fast5_subset", "hdf2tf.py": "/usr/local/bin/hdf2tf.py", "import_pb_to_tensorboard": "/usr/local/bin/import_pb_to_tensorboard", "medaka": "/usr/local/bin/medaka", "medaka_consensus": "/usr/local/bin/medaka_consensus", "medaka_counts": "/usr/local/bin/medaka_counts", "medaka_data_path": "/usr/local/bin/medaka_data_path", "medaka_haploid_variant": "/usr/local/bin/medaka_haploid_variant", "medaka_version_report": "/usr/local/bin/medaka_version_report", "mini_align": "/usr/local/bin/mini_align", "multi_to_single_fast5": "/usr/local/bin/multi_to_single_fast5", "piranha": "/usr/local/bin/piranha", "piranha_preprocessing.smk": "/usr/local/bin/piranha_preprocessing.smk", "piranha_vp1.smk": "/usr/local/bin/piranha_vp1.smk", "piranha_wg_2tile.smk": "/usr/local/bin/piranha_wg_2tile.smk", "single_to_multi_fast5": "/usr/local/bin/single_to_multi_fast5", "snipit": "/usr/local/bin/snipit", "snipit.smk": "/usr/local/bin/snipit.smk", "snp_functions.py": "/usr/local/bin/snp_functions.py", "variation.smk": "/usr/local/bin/variation.smk", "aec": "/usr/local/bin/aec", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "minimap2.py": "/usr/local/bin/minimap2.py", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "mako-render": "/usr/local/bin/mako-render", "docutils": "/usr/local/bin/docutils", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "tar": "/usr/local/bin/tar", "gff2gff.py": "/usr/local/bin/gff2gff.py", "pulptest": "/usr/local/bin/pulptest", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco", "toco_from_protos": "/usr/local/bin/toco_from_protos"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piranha-polio.
singularity registry hpc automated addition for piranha-polio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piranha-polio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piranha-polio:1.0.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piranha-polio/1.0.8--pyhdfd78af_0
$ module help quay.io/biocontainers/piranha-polio/1.0.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piranha-polio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piranha-polio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piranha-polio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piranha-polio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piranha-polio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piranha-polio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_compression

```bash
$ singularity exec <container> /usr/local/bin/check_compression
$ podman run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress_fast5

```bash
$ singularity exec <container> /usr/local/bin/compress_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus.smk

```bash
$ singularity exec <container> /usr/local/bin/consensus.smk
$ podman run --it --rm --entrypoint /usr/local/bin/consensus.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux_fast5

```bash
$ singularity exec <container> /usr/local/bin/demux_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast5_subset

```bash
$ singularity exec <container> /usr/local/bin/fast5_subset
$ podman run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2tf.py

```bash
$ singularity exec <container> /usr/local/bin/hdf2tf.py
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_pb_to_tensorboard

```bash
$ singularity exec <container> /usr/local/bin/import_pb_to_tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka

```bash
$ singularity exec <container> /usr/local/bin/medaka
$ podman run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_consensus

```bash
$ singularity exec <container> /usr/local/bin/medaka_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_counts

```bash
$ singularity exec <container> /usr/local/bin/medaka_counts
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_data_path

```bash
$ singularity exec <container> /usr/local/bin/medaka_data_path
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_haploid_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_haploid_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_version_report

```bash
$ singularity exec <container> /usr/local/bin/medaka_version_report
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_align

```bash
$ singularity exec <container> /usr/local/bin/mini_align
$ podman run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_to_single_fast5

```bash
$ singularity exec <container> /usr/local/bin/multi_to_single_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piranha

```bash
$ singularity exec <container> /usr/local/bin/piranha
$ podman run --it --rm --entrypoint /usr/local/bin/piranha   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piranha   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piranha_preprocessing.smk

```bash
$ singularity exec <container> /usr/local/bin/piranha_preprocessing.smk
$ podman run --it --rm --entrypoint /usr/local/bin/piranha_preprocessing.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piranha_preprocessing.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piranha_vp1.smk

```bash
$ singularity exec <container> /usr/local/bin/piranha_vp1.smk
$ podman run --it --rm --entrypoint /usr/local/bin/piranha_vp1.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piranha_vp1.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piranha_wg_2tile.smk

```bash
$ singularity exec <container> /usr/local/bin/piranha_wg_2tile.smk
$ podman run --it --rm --entrypoint /usr/local/bin/piranha_wg_2tile.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piranha_wg_2tile.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_to_multi_fast5

```bash
$ singularity exec <container> /usr/local/bin/single_to_multi_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snipit

```bash
$ singularity exec <container> /usr/local/bin/snipit
$ podman run --it --rm --entrypoint /usr/local/bin/snipit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snipit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snipit.smk

```bash
$ singularity exec <container> /usr/local/bin/snipit.smk
$ podman run --it --rm --entrypoint /usr/local/bin/snipit.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snipit.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp_functions.py

```bash
$ singularity exec <container> /usr/local/bin/snp_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/snp_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variation.smk

```bash
$ singularity exec <container> /usr/local/bin/variation.smk
$ podman run --it --rm --entrypoint /usr/local/bin/variation.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variation.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aec

```bash
$ singularity exec <container> /usr/local/bin/aec
$ podman run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimator_ckpt_converter

```bash
$ singularity exec <container> /usr/local/bin/estimator_ckpt_converter
$ podman run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_objective_c_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_objective_c_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_php_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_php_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_python_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_python_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_ruby_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_ruby_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tflite_convert

```bash
$ singularity exec <container> /usr/local/bin/tflite_convert
$ podman run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saved_model_cli

```bash
$ singularity exec <container> /usr/local/bin/saved_model_cli
$ podman run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco

```bash
$ singularity exec <container> /usr/local/bin/toco
$ podman run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco_from_protos

```bash
$ singularity exec <container> /usr/local/bin/toco_from_protos
$ podman run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
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