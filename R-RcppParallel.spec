#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: e661f3a
#
Name     : R-RcppParallel
Version  : 5.1.7
Release  : 43
URL      : https://cran.r-project.org/src/contrib/RcppParallel_5.1.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcppParallel_5.1.7.tar.gz
Summary  : Parallel Programming Tools for 'Rcpp'
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
Requires: R-RcppParallel-lib = %{version}-%{release}
Requires: R-RcppParallel-license = %{version}-%{release}
Requires: tbb
Requires: tbb-dev
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
For example, the 'parallelFor()' function can be used to convert the work of
    a standard serial "for" loop into a parallel one and the 'parallelReduce()'
    function can be used for accumulating aggregate or other values.

%package lib
Summary: lib components for the R-RcppParallel package.
Group: Libraries
Requires: R-RcppParallel-license = %{version}-%{release}

%description lib
lib components for the R-RcppParallel package.


%package license
Summary: license components for the R-RcppParallel package.
Group: Default

%description license
license components for the R-RcppParallel package.


%prep
%setup -q -n RcppParallel
pushd ..
cp -a RcppParallel buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701370693

%install
export SOURCE_DATE_EPOCH=1701370693
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-RcppParallel
cp %{_builddir}/RcppParallel/src/tbb/COPYING %{buildroot}/usr/share/package-licenses/R-RcppParallel/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/RcppParallel/src/tbb/LICENSE %{buildroot}/usr/share/package-licenses/R-RcppParallel/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppParallel/DESCRIPTION
/usr/lib64/R/library/RcppParallel/INDEX
/usr/lib64/R/library/RcppParallel/Meta/Rd.rds
/usr/lib64/R/library/RcppParallel/Meta/features.rds
/usr/lib64/R/library/RcppParallel/Meta/hsearch.rds
/usr/lib64/R/library/RcppParallel/Meta/links.rds
/usr/lib64/R/library/RcppParallel/Meta/nsInfo.rds
/usr/lib64/R/library/RcppParallel/Meta/package.rds
/usr/lib64/R/library/RcppParallel/NAMESPACE
/usr/lib64/R/library/RcppParallel/NEWS.md
/usr/lib64/R/library/RcppParallel/R/RcppParallel
/usr/lib64/R/library/RcppParallel/R/RcppParallel.rdb
/usr/lib64/R/library/RcppParallel/R/RcppParallel.rdx
/usr/lib64/R/library/RcppParallel/help/AnIndex
/usr/lib64/R/library/RcppParallel/help/RcppParallel.rdb
/usr/lib64/R/library/RcppParallel/help/RcppParallel.rdx
/usr/lib64/R/library/RcppParallel/help/aliases.rds
/usr/lib64/R/library/RcppParallel/help/paths.rds
/usr/lib64/R/library/RcppParallel/html/00Index.html
/usr/lib64/R/library/RcppParallel/html/R.css
/usr/lib64/R/library/RcppParallel/include/RcppParallel.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/Backend.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/Common.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/RMatrix.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/RVector.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/TBB.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/Timer.h
/usr/lib64/R/library/RcppParallel/include/RcppParallel/TinyThread.h
/usr/lib64/R/library/RcppParallel/include/index.html
/usr/lib64/R/library/RcppParallel/include/serial/tbb/parallel_for.h
/usr/lib64/R/library/RcppParallel/include/serial/tbb/tbb_annotate.h
/usr/lib64/R/library/RcppParallel/include/tbb/aggregator.h
/usr/lib64/R/library/RcppParallel/include/tbb/aligned_space.h
/usr/lib64/R/library/RcppParallel/include/tbb/atomic.h
/usr/lib64/R/library/RcppParallel/include/tbb/blocked_range.h
/usr/lib64/R/library/RcppParallel/include/tbb/blocked_range2d.h
/usr/lib64/R/library/RcppParallel/include/tbb/blocked_range3d.h
/usr/lib64/R/library/RcppParallel/include/tbb/blocked_rangeNd.h
/usr/lib64/R/library/RcppParallel/include/tbb/cache_aligned_allocator.h
/usr/lib64/R/library/RcppParallel/include/tbb/combinable.h
/usr/lib64/R/library/RcppParallel/include/tbb/compat/condition_variable
/usr/lib64/R/library/RcppParallel/include/tbb/compat/iterator.h
/usr/lib64/R/library/RcppParallel/include/tbb/compat/ppl.h
/usr/lib64/R/library/RcppParallel/include/tbb/compat/thread
/usr/lib64/R/library/RcppParallel/include/tbb/compat/tuple
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_hash_map.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_lru_cache.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_map.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_priority_queue.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_queue.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_set.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_unordered_map.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_unordered_set.h
/usr/lib64/R/library/RcppParallel/include/tbb/concurrent_vector.h
/usr/lib64/R/library/RcppParallel/include/tbb/critical_section.h
/usr/lib64/R/library/RcppParallel/include/tbb/enumerable_thread_specific.h
/usr/lib64/R/library/RcppParallel/include/tbb/flow_graph.h
/usr/lib64/R/library/RcppParallel/include/tbb/flow_graph_abstractions.h
/usr/lib64/R/library/RcppParallel/include/tbb/flow_graph_opencl_node.h
/usr/lib64/R/library/RcppParallel/include/tbb/gfx_factory.h
/usr/lib64/R/library/RcppParallel/include/tbb/global_control.h
/usr/lib64/R/library/RcppParallel/include/tbb/index.html
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_aggregator_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_allocator_traits.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_concurrent_queue_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_concurrent_skip_list_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_concurrent_unordered_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_async_msg_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_body_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_cache_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_indexer_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_item_buffer_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_join_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_node_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_streaming_node.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_tagged_buffer_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_trace_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_flow_graph_types_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_mutex_padding.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_node_handle_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_range_iterator.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_tbb_hash_compare_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_tbb_strings.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_tbb_trace_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_tbb_windef.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_template_helpers.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_x86_eliding_mutex_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/internal/_x86_rtm_rw_mutex_impl.h
/usr/lib64/R/library/RcppParallel/include/tbb/iterators.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/gcc_arm.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/gcc_armv7.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/gcc_generic.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/gcc_ia32_common.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/gcc_itsx.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/ibm_aix51.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/icc_generic.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/linux_common.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/linux_ia32.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/linux_ia64.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/linux_intel64.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/mac_ppc.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/macos_common.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/mic_common.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/msvc_armv7.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/msvc_ia32_common.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/sunos_sparc.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/windows_api.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/windows_ia32.h
/usr/lib64/R/library/RcppParallel/include/tbb/machine/windows_intel64.h
/usr/lib64/R/library/RcppParallel/include/tbb/memory_pool.h
/usr/lib64/R/library/RcppParallel/include/tbb/mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/null_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/null_rw_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_do.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_for.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_for_each.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_invoke.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_reduce.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_scan.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_sort.h
/usr/lib64/R/library/RcppParallel/include/tbb/parallel_while.h
/usr/lib64/R/library/RcppParallel/include/tbb/partitioner.h
/usr/lib64/R/library/RcppParallel/include/tbb/pipeline.h
/usr/lib64/R/library/RcppParallel/include/tbb/queuing_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/queuing_rw_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/reader_writer_lock.h
/usr/lib64/R/library/RcppParallel/include/tbb/recursive_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/runtime_loader.h
/usr/lib64/R/library/RcppParallel/include/tbb/scalable_allocator.h
/usr/lib64/R/library/RcppParallel/include/tbb/spin_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/spin_rw_mutex.h
/usr/lib64/R/library/RcppParallel/include/tbb/task.h
/usr/lib64/R/library/RcppParallel/include/tbb/task_arena.h
/usr/lib64/R/library/RcppParallel/include/tbb/task_group.h
/usr/lib64/R/library/RcppParallel/include/tbb/task_scheduler_init.h
/usr/lib64/R/library/RcppParallel/include/tbb/task_scheduler_observer.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_allocator.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_config.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_disable_exceptions.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_exception.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_machine.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_profiling.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_stddef.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbb_thread.h
/usr/lib64/R/library/RcppParallel/include/tbb/tbbmalloc_proxy.h
/usr/lib64/R/library/RcppParallel/include/tbb/tick_count.h
/usr/lib64/R/library/RcppParallel/include/tthread/fast_mutex.h
/usr/lib64/R/library/RcppParallel/include/tthread/tinythread.h
/usr/lib64/R/library/RcppParallel/include/tthread/tinythread.inl
/usr/lib64/R/library/RcppParallel/presentations/header.tex
/usr/lib64/R/library/RcppParallel/presentations/images/big-data-big-machine-tweet.png
/usr/lib64/R/library/RcppParallel/presentations/rcpp_parallel_talk_jan2015.Rmd
/usr/lib64/R/library/RcppParallel/rstudio/templates/project/RcppParallel.package.skeleton.dcf
/usr/lib64/R/library/RcppParallel/skeleton/vector-sum.Rd
/usr/lib64/R/library/RcppParallel/skeleton/vector-sum.cpp
/usr/lib64/R/library/RcppParallel/tests/cpp/distance.cpp
/usr/lib64/R/library/RcppParallel/tests/cpp/innerproduct.cpp
/usr/lib64/R/library/RcppParallel/tests/cpp/sum.cpp
/usr/lib64/R/library/RcppParallel/tests/cpp/transform.cpp
/usr/lib64/R/library/RcppParallel/tests/doRUnit.R
/usr/lib64/R/library/RcppParallel/tests/runit.distance.R
/usr/lib64/R/library/RcppParallel/tests/runit.innerproduct.R
/usr/lib64/R/library/RcppParallel/tests/runit.sum.R
/usr/lib64/R/library/RcppParallel/tests/runit.transform.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppParallel/lib/libtbb.so
/usr/lib64/R/library/RcppParallel/lib/libtbb.so.2
/usr/lib64/R/library/RcppParallel/lib/libtbbmalloc.so
/usr/lib64/R/library/RcppParallel/lib/libtbbmalloc.so.2
/usr/lib64/R/library/RcppParallel/lib/libtbbmalloc_proxy.so
/usr/lib64/R/library/RcppParallel/lib/libtbbmalloc_proxy.so.2
/usr/lib64/R/library/RcppParallel/libs/RcppParallel.so
/usr/lib64/R/library/RcppParallel/libs/RcppParallel.so.avx2
/usr/lib64/R/library/RcppParallel/libs/RcppParallel.so.avx512
/usr/lib64/R/library/RcppParallel/libs/libtbb.so.avx2
/usr/lib64/R/library/RcppParallel/libs/libtbb.so.avx512
/usr/lib64/R/library/RcppParallel/libs/libtbbmalloc.so.avx2
/usr/lib64/R/library/RcppParallel/libs/libtbbmalloc.so.avx512
/usr/lib64/R/library/RcppParallel/libs/libtbbmalloc_proxy.so.avx2
/usr/lib64/R/library/RcppParallel/libs/libtbbmalloc_proxy.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-RcppParallel/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
