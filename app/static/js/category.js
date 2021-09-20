
layui.use('table', function () {
    var table = layui.table;

    table.render({
        elem: '#categories-table'
        , url: '/admin/categories'
        , title: '分类列表'
        , cols: [[

            {field: 'id', title: 'ID', width: 80, fixed: 'left', unresize: true, sort: true}
            , {field: 'name', title: '分类名称', width: 120, edit: 'text'}
            , {field: 'slug', title: '分类别名', width: 120, edit: 'text'}
            , {field: 'description', title: '分类描述', width: 120,edit: 'text'}
            , {fixed: 'right', title: '操作', toolbar: '#barDemo', width: 150}
        ]]
        , page: true
    });

    //监听行工具事件
    table.on('tool(categories-table)', function (obj) {
        var data = obj.data;
        //console.log(obj)
        if (obj.event === 'del') {
            layer.confirm('真的删除行么', function (index) {
                obj.del();
                layer.close(index);
            });
        } else if (obj.event === 'edit') {
            layer.prompt({
                formType: 2
                , value: data.email
            }, function (value, index) {
                obj.update({
                    email: value
                });
                layer.close(index);
            });
        }
    });
});

