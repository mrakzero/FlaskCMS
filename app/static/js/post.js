
layui.use('table', function(){
  var table = layui.table;

  table.render({
    elem: '#posts-table'
    ,url: '/admin/posts' //数据接口
    ,parseData: function(res){ //res 即为原始返回的数据
      console.log(res.data.code)
      console.log(res.data.message)
      console.log(res.data.posts)
    return {
      "code": res.data.code, //解析接口状态
      "msg": res.data.message, //解析提示文本
      // "count": res.total, //解析数据长度
      "data": res.data.posts //解析数据列表
    };
  }
    // 设置响应数据字段名称
    ,response: {
        statusCode: 20000000 //规定成功的状态码，默认：0
        ,msgName: 'message' //规定状态信息的字段名称，默认：msg
        ,dataName: 'posts' //规定数据列表的字段名称，默认：data
    }
    ,page: true //开启分页
    ,cols: [[ //表头
      {field: 'post_id', title: 'ID', width:80, sort: true, fixed: 'left'}
      ,{field: 'post_title', title: '标题', width:80}
      ,{field: 'post_category', title: '分类', width:80}
      ,{field: 'post_author', title: '作者', width:80}
      ,{field: 'post_status', title: '状态', width: 177}
      ,{field: 'post_publishtime', title: '发布时间', width: 177}
      ,{field: 'post_updatetime', title: '更新时间', width: 177}
    ]]
  });

});



