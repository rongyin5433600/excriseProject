from django.utils.safestring import mark_safe
import copy


class Pagination(object):
    def __init__(self, request, queryset, parm_get='page', plus=5, page_size=10):
        """
            :param request: 请求对象
            :param queryset: 符合条件的数据集（需要分页的数据集合）
            :param parm_get: 在url中传递的分页参数此处为page
            :param plus: 页面显示时需要显示当前页面的前几后几页
            :param page_size: 每页显示多少条数据
        """
        """ 获取前端的查询条件为后续标签按钮url拼接使用 """
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        """ 获取传入的page以及根据queryset计算出总页数 """
        page = str(request.GET.get(parm_get))
        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count

        """ 对page参数处理考虑为空或者不为数字的情况 """
        if page == '':
            page = 1
        else:
            if page.isdigit():
                if int(page) >= self.total_page_count:
                    page = self.total_page_count
                else:
                    pass
            else:
                page = 1
        self.parm_get = parm_get
        self.page = int(page)
        self.page_size = page_size
        self.start = (self.page - 1) * self.page_size
        self.end = self.page * self.page_size
        self.page_queryset = queryset[self.start:self.end]
        self.plus = plus

    def html(self):
        if self.total_page_count < self.plus * 2 + 1:
            self.startpage = 1
            self.endpage = self.total_page_count
        else:
            if self.page - self.plus <= 0:
                self.startpage = 1
                if self.page + self.plus >= self.total_page_count:
                    self.endpage = self.total_page_count
                else:
                    self.endpage = self.plus * 2 + 1
            else:
                self.startpage = self.page - self.plus
                if self.page + 5 >= self.total_page_count:
                    self.startpage = self.total_page_count - self.plus * 2
                    self.endpage = self.total_page_count
                else:
                    self.endpage = self.page + self.plus
        page_str_list = []
        ''' 首页标签 '''
        self.query_dict.setlist(self.parm_get,[1])
        ele = '<li><a href="?{}" aria-label="Previous"><span class="glyphicon glyphicon-fast-backward" ' \
              'aria-hidden="true"></span></a></li> '.format(self.query_dict.urlencode())
        page_str_list.append(ele)
        ''' 上一页标签 '''
        if self.page > 1:
            self.query_dict.setlist(self.parm_get,[self.page - 1])
            ele = '<li><a href="?{}" aria-label="Previous"><span class="glyphicon glyphicon-backward" ' \
                  'aria-hidden="true"></span></a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.parm_get, [1])
            ele = '<li><a href="?{}" aria-label="Previous"><span class="glyphicon glyphicon-backward" ' \
                  'aria-hidden="true"></span></a></li> '.format(self.query_dict.urlencode())
        page_str_list.append(ele)

        ''' 页数标签 '''
        for i in range(self.startpage, self.endpage + 1):
            if self.page == i:
                self.query_dict.setlist(self.parm_get, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.parm_get, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        ''' 下一页标签 '''
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.parm_get, [self.page + 1])
            ele = '<li><a href="?{}" aria-label="Previous"><span class="glyphicon glyphicon-forward" ' \
                  'aria-hidden="true"></span></a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.parm_get, [self.total_page_count])
            ele = '<li><a href="?{}" aria-label="Previous"><span class="glyphicon glyphicon-forward" ' \
                  'aria-hidden="true"></span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(ele)

        ''' 尾页标签 '''
        self.query_dict.setlist(self.parm_get, [self.total_page_count])
        ele = '<li><a href="?{}" aria-label="Previous"><span class="glyphicon glyphicon-fast-forward" ' \
              'aria-hidden="true"></span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(ele)

        ele = '''
        <li>
                    <form style="float: left;margin-left: -1px" method="get">
                        <input name="page"
                               style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0;"
                               type="text" class="form-control" placeholder="页码"/>
                        <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                    </form>
                </li>
        '''
        page_str_list.append(ele)
        page_string = mark_safe("".join(page_str_list))

        return page_string
